import json
from password_check import check
from salt import salt_password, generate_salt


# For registration
def reg(request, psql):
    firstname, lastname = request.body["firstname"], request.body["lastname"]
    salt = generate_salt()
    mail, password = request.body["login"], \
        salt_password(request.body["password"], salt)
    ans = check(firstname, lastname, mail, password)
    if sum(ans.values()) == 4:
        psql.add_user(firstname, lastname, mail, password, salt)
        return json.dumps(ans)
    return json.dumps(ans)
