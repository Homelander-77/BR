import json
from response import MakeHTTPResponse
from cookie import cookie_create
from salt import verify_password


def login(request, database):
    in_login, in_password = request.body["login"], request.body["password"]
    if verify_password(in_login, in_password, database):
        ans = json.dumps({"success": True})
        cookie = cookie_create()
        response = MakeHTTPResponse(200, ans).make(cookie=cookie)
        database.add_cookie(in_login, cookie)
        print('{"success": true}')
        return response
    else:
        ans = json.dumps({"success": False})
        response = MakeHTTPResponse(401, ans).make(cookie=False)
        print('{"success": false}')
        return response
