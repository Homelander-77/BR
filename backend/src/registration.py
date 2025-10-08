import json
from password_check import check
from salt import salt_password, generate_salt
from response import MakeHTTPResponse
from cookie import cookie_create


def reg(request, database):
    firstname, lastname = request.body["firstname"], request.body["lastname"]
    mail, password = request.body["login"], request.body["password"]
    ans = check(firstname, lastname, mail, password)
    if sum(ans.values()) == 4:
        salt = generate_salt()
        password = salt_password(password, salt)
        cookie = cookie_create()
        database.add_user(firstname, lastname, mail, password, salt, cookie)
        response = MakeHTTPResponse(200, json.dumps(ans)).make(cookie=cookie)
        return response
    response = MakeHTTPResponse(400, json.dumps(ans)).make(cookie={})
    return response
