import json
from response import MakeHTTPResponse


def rec(request, database):
    ans = json.dumps(database.get_rec())
    response = MakeHTTPResponse(200, ans).make()
    return response
