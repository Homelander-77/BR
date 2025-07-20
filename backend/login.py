import json


def login(request, database):
    print(request.body)
    if len(request.body) > 0 and database.check_auth(request.body["login"], \
                                                     request.body["password"]):
        print('{"success": true}')
        return json.dumps({"success": True}), 200
    else:
        print('{"success": false}')
        return json.dumps({"success": False}), 401
