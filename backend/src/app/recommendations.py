import http
import json

from utils.response import MakeHTTPResponse
from postgres import Database


def rec(request):
    pg = Database()
    ans = dict(pg.execute_func('get_recommendations', ())[0][0])
    response = MakeHTTPResponse(http.HTTPStatus.OK, ans).make()
    return response
