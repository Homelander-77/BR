import json
import http

from response import MakeHTTPResponse
from cookie import cookie_create
from salt import verify_password


def login(request, database):
    print(request.body)
    in_login, in_password = request.body["login"], request.body["password"]
    if verify_password(in_login, in_password, database):
        ans = json.dumps({"success": True})
        cookie = cookie_create()
        response = MakeHTTPResponse(http.HTTPStatus.OK, ans).make(cookie=cookie)
        database.add_cookie(in_login, cookie)
        print('{"success": true}')
        return response
    else:
        ans = json.dumps({"success": False})
        response = MakeHTTPResponse(http.HTTPStatus.UNAUTHORIZED, ans).make()
        print('{"success": false}')
        return response
