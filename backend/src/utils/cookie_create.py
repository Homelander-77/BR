import uuid
from datetime import datetime, timedelta


def cookie_create():
    time_sample = "%a, %d %b %Y %H:%M:%S GMT"
    cookie_id = str(uuid.uuid4())
    expire = (datetime.utcnow() + timedelta(days=7)).strftime(time_sample)
    return {'id': cookie_id, 'expire': expire}
