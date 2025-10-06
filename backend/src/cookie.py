import uuid
from datetime import datetime, timedelta
from response import MakeHTTPResponse


def cookie_check(request, database):
    if 'Cookie' in request.headers:
        cookie = str(dict([tuple(i.split('=')) for i in request.headers['Cookie'].split('; ')])['id'])
        time = database.get_cookie_expire(cookie)
        if time:
            expire = datetime.strptime(time, "%a, %d %b %Y %H:%M:%S GMT")
            if datetime.utcnow() < expire:
                return MakeHTTPResponse(200, '').make()
    return MakeHTTPResponse(403, '').make()


def cookie_create():
    cookie_id = str(uuid.uuid4())
    expire = (datetime.utcnow() + timedelta(days=7)).strftime("%a, %d %b %Y %H:%M:%S GMT")
    return {'id': cookie_id, 'expire': expire}
