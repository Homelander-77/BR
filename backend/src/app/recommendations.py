import http

from utils.HTTPResponse import HTTPResponse
from database_manager import pg


def rec(request):
    ans = dict(pg.execute_func('get_recommendations')[0][0])
    response = HTTPResponse(http.HTTPStatus.OK, ans).make()
    return response
