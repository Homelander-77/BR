import uuid
from datetime import datetime, timedelta


def cookie_check(request, psql):
    pass


def cookie_create():
    cookie_id = str(uuid.uuid4())
    expire = (datetime.utcnow() + timedelta(days=7)).strftime("%a, %d %b %Y %H:%M:%S GMT")
    return {'id': cookie_id, 'expire': expire}
