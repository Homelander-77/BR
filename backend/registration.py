from password_check import check
import json


def analysis(request, *args, **kwargs):
    firstname, lastname = request.body["firstname"], request.body["lastname"]
    mail, password = request.body["login"], request.body["password"]
    ans = check(firstname, lastname, mail, password)
    return json.dumps(ans)


def reg(request, psql):
    firstname, lastname = request.body["firstname"], request.body["lastname"]
    mail, password = request.body["login"], request.body["password"]
    ans = check(firstname, lastname, mail, password)
    if sum(ans.values()) == 4:
        psql.add_user(firstname, lastname, mail, password)
        return json.dumps(ans)
    return json.dumps(ans)
