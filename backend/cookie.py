import uuid
from datetime import datetime, timedelta
from response import MakeHTTPResponse


def cookie_check(request, database):
    cookie = dict([tuple(i.split('=')) for i in request.headers['Cookie'].split('; ')])['id']
    if cookie:
        expire = datetime.strptime(database.get_cookie_expire(cookie), "%a, %d %b %Y %H:%M:%S GMT")
        if datetime.utcnow() < expire:
            return MakeHTTPResponse(200, '').make()
    return MakeHTTPResponse(403, '').make()


def cookie_create():
    cookie_id = str(uuid.uuid4())
    expire = (datetime.utcnow() + timedelta(days=7)).strftime("%a, %d %b %Y %H:%M:%S GMT")
    return {'id': cookie_id, 'expire': expire}
