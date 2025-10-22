import json
import http

from utils.password_check import check
from utils.salt import salt_password, generate_salt
from utils.response import MakeHTTPResponse
from utils.cookie_create import cookie_create
from .postgres import Database


def reg(request):
    pg = Database()
    firstname, lastname = request.body["firstname"], request.body["lastname"]
    mail, password = request.body["login"], request.body["password"]
    ans = check(firstname, lastname, mail, password)
    if sum(ans.values()) == 4:
        salt = generate_salt()
        password = salt_password(password, salt)
        cookie = cookie_create()
        pg.add_user(firstname, lastname, mail, password, salt, cookie)
        response = MakeHTTPResponse(http.HTTPStatus.OK, json.dumps(ans)).make(cookie=cookie)
        return response
    response = MakeHTTPResponse(http.HTTPStatus.NOT_FOUND, json.dumps(ans)).make(cookie={})
    return response
