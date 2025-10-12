import http
import json

from utils.response import MakeHTTPResponse


def rec(request, database):
    ans = json.dumps(database.get_rec())
    response = MakeHTTPResponse(http.HTTPStatus.OK, ans).make()
    return response
