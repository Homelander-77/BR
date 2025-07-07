from password_check import check
import json


def reg(request, psql):
    ans = check(mail=request.body["login"], password=request.body["password"])
    if sum(ans.values()) == 4:
        return json.dumps(ans)
    return json.dumps(ans)
