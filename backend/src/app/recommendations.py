import http
import json

from utils.response import MakeHTTPResponse
from .postgres import Database


def rec(request):
    pg = Database()
    ans = json.dumps(pg.get_rec())
    response = MakeHTTPResponse(http.HTTPStatus.OK, ans).make()
    return response
