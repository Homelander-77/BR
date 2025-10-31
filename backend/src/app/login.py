import json
import http

from utils.HTTPResponse import HTTPResponse
from utils.cookie_create import cookie_create
from utils.salt import salt_password
from postgres import Database
import redis_server


def verify_password(input_login, input_password):
    pg = Database()
    password = pg.execute_func("get_password_by_login", input_login)
    print(input_login, input_password)
    if password:
        input_salt = pg.execute_func("get_salt_by_login", login)
        input_hash = salt_password(input_password, input_salt)
        return pg.execute_func("get_user_id_by_login", input_login) if input_hash == password else 0
    else:
        return 0


def login(request):
    print(request.body)
    in_login, in_password = request.body["login"], request.body["password"]
    user_id = verify_password(in_login, in_password)
    if user_id:
        ans = json.dumps({"success": True})
        cookie = cookie_create()
        response = HTTPResponse(http.HTTPStatus.OK, ans).make(cookie=cookie)
        redis_server.set_key_value({"user_id": user_id, "cookie": cookie})
        print('{"success": true}')
        return response
    else:
        ans = json.dumps({"success": False})
        response = HTTPResponse(http.HTTPStatus.UNAUTHORIZED, ans).make()
        print('{"success": false}')
        return response
