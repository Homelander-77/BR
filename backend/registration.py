import json
from password_check import check
from salt import salt_password, generate_salt
from response import MakeHTTPResponse


def reg(request, psql):
    firstname, lastname = request.body["firstname"], request.body["lastname"]
    mail, password = request.body["login"], request.body["password"]
    ans = check(firstname, lastname, mail, password)
    if sum(ans.values()) == 4:
        salt = generate_salt()
        password = salt_password(password, salt)
        psql.add_user(firstname, lastname, mail, password, salt)
        response = MakeHTTPResponse(200, json.dumps(ans)).make(cookie=True)
        return response
    response = MakeHTTPResponse(400, json.dumps(ans)).make(cookie=False)
    return response
