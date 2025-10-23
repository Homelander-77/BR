import http

from datetime import datetime
from utils.response import MakeHTTPResponse
from ..postgres import Database


def cookie_check(request):
    pg = Database()
    time_sample = "%a, %d %b %Y %H:%M:%S GMT"
    if 'Cookie' in request.headers:
        cookie = str(dict([tuple(i.split('=')) for i in request.headers['Cookie'].split('; ')])['id'])
        time = pg.execute_func("get_cookie_expire", cookie)
        if time:
            expire = datetime.strptime(time, time_sample)
            if datetime.utcnow() < expire:
                return MakeHTTPResponse(http.HTTPStatus.OK, '').make()
    return MakeHTTPResponse(http.HTTPStatus.FORBIDDEN, '').make()
