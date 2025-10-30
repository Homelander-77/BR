import json
import http

from utils.password_check import check
from utils.salt import salt_password, generate_salt
from utils.HTTPResponse import HTTPResponse
from utils.cookie_create import cookie_create
from postgres import Database
import redis


def reg(request):
    pg = Database()
    firstname, lastname = request.body["firstname"], request.body["lastname"]
    login, password = request.body["login"], request.body["password"]
    ans = check(firstname, lastname, login, password)
    if pg.execute_func("check_user_existing", login):
        return HTTPResponse(http.HTTPStatus.CONFLICT, json.dumps(ans)).make(cookie={})
    if sum(ans.values()) == 5:
        salt = generate_salt()
        password = salt_password(password, salt)
        cookie = cookie_create()
        user_id = pg.execute_func("add_user", firstname, lastname, login, password)
        redis.set_key_value({"user_id": user_id, "cookie": cookie})
        return HTTPResponse(http.HTTPStatus.OK, json.dumps(ans)).make(cookie=cookie)
    return HTTPResponse(http.HTTPStatus.UNAUTHORIZED, json.dumps(ans)).make(cookie={})
