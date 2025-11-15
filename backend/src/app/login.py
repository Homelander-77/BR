import json
import http
from datetime import datetime

from utils.HTTPResponse import HTTPResponse
from utils.cookie_create import cookie_create, create_expire
from utils.salt import salt_password
from database_manager import pg
from session_manager import redis
from logger_manager import sub_logger, general_loger


time_sample = "%a, %d %b %Y %H:%M:%S GMT"


def check_auth(request):
    if 'Cookie' in request.headers:
        session_id = str(dict(
            [tuple(i.split('='))
             for i in request.headers['Cookie'].split('; ')])
            ['session_id'])
        expire = redis.get_value(session_id, "expire")
        if expire:
            expire = datetime.strptime(expire, time_sample)
            if datetime.utcnow() < expire:
                new_expire = create_expire()
                redis.set_key_value({
                    "session_id": session_id,
                    "expire": new_expire})
                return HTTPResponse(http.HTTPStatus.OK, '').make(cookie={
                    "session_id": session_id,
                    "expire": new_expire})
    return HTTPResponse(http.HTTPStatus.FORBIDDEN, '').make(cookie={})


def verify_password(input_login, input_password):
    try:
        password = pg.execute_func("get_password_by_login", input_login)
        if not password:
            raise ValueError
    except ValueError:
        sub_logger["login"].info(f"No password with login {input_login}")
        return 0

    input_salt = pg.execute_func("get_salt_by_login", login)
    input_hash = salt_password(input_password, input_salt)
    return (pg.execute_func("get_user_id_by_login", input_login)
            if input_hash == password
            else 0)        


def login(request):
    general_loger.info(f"Accepted connection, request body {request.body}")
    in_login, in_password = request.body["login"], request.body["password"]
    user_id = verify_password(in_login, in_password)
    if user_id:
        ans = json.dumps({"success": True})
        cookie = cookie_create()
        redis.set_key_value({
            "session_id": cookie['session_id'],
            "user_id": user_id,
            "expire": cookie['expire']})
        response = HTTPResponse(http.HTTPStatus.OK, ans).make(cookie=cookie)
        print('{"success": true}')
        return response
    else:
        ans = json.dumps({"success": False})
        response = HTTPResponse(
            http.HTTPStatus.UNAUTHORIZED, ans
            ).make(cookie={})
        print('{"success": false}')
        return response
