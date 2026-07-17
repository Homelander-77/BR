import http

from utils.HTTPResponse import HTTPResponse
from postgres import Database


def rec(request):
    pg = Database()
    ans = dict(pg.execute_func('get_recommendations', ())[0][0])
    response = HTTPResponse(http.HTTPStatus.OK, ans).make()
    return response
