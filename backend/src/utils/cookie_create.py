import uuid
from datetime import datetime, timedelta

time_sample = "%a, %d %b %Y %H:%M:%S GMT"


def create_expire():
    return (datetime.utcnow() + timedelta(days=7)).strftime(time_sample)


def cookie_create():
    session_id = str(uuid.uuid4())
    expire = create_expire()
    return {'session_id': session_id, 'expire': expire}
