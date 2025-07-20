import json
from password_check import check
from salt import salt_password, generate_salt


def reg(request, psql):
    firstname, lastname = request.body["firstname"], request.body["lastname"]
    mail, password = request.body["login"], request.body["password"]
    ans = check(firstname, lastname, mail, password)
    if sum(ans.values()) == 4:
        salt = generate_salt()
        password = salt_password(password, salt)
        print(firstname, lastname, mail, password, salt)
        psql.add_user(firstname, lastname, mail, password, salt)
        return json.dumps(ans), 200
    return json.dumps(ans), 400
