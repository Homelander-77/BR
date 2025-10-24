import json
import http

from utils.response import MakeHTTPResponse
from utils.cookie_create import cookie_create
from utils.salt import salt_password
from postgres import Database


def verify_password(input_login, input_password):
    pg = Database()
    password = pg.execute_func("get_password_by_login", input_login)
    print(input_login, input_password)
    if password:
        input_salt = pg.execute_func("get_salt_by_login", login)
        input_hash = salt_password(input_password, input_salt)
        return input_hash == password
    else:
        return False


def login(request):
    print(request.body)
    in_login, in_password = request.body["login"], request.body["password"]
    if verify_password(in_login, in_password):
        pg = Database()
        ans = json.dumps({"success": True})
        cookie = cookie_create()
        response = MakeHTTPResponse(http.HTTPStatus.OK, ans).make(cookie=cookie)
        pg.execute_func("set_cookie", in_login, cookie)
        print('{"success": true}')
        return response
    else:
        ans = json.dumps({"success": False})
        response = MakeHTTPResponse(http.HTTPStatus.UNAUTHORIZED, ans).make()
        print('{"success": false}')
        return response
