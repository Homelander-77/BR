import json
from response import MakeHTTPResponse


def login(request, database):
    print(request.body)
    if len(request.body) > 0 and database.check_auth(request.body["login"], \
                                                     request.body["password"]):
        ans = json.dumps({"success": True}), 200
        response = MakeHTTPResponse(200, ans).make(cookie=True)
        print('{"success": true}')
        return response
    else:
        ans = json.dumps({"success": False})
        response = MakeHTTPResponse(401, ans).make(cookie=False)
        print('{"success": false}')
        return response
