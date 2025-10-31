import threading
import redis
import uuid

from lazy_start import lazy_start
from config import redis_conf


class Redis:
    __instance = None
    _lock = threading.lock()

    def __new__(cls):
        with cls._lock:
            if cls.__instance is None:
                cls.__instance = super(Redis, cls).__new__(cls)
            return cls.__instance

    def __init__(self):
        self.redis = None

    def connect(self):
        self.redis = redis.Redis(
            host=redis_conf['host'],
            port=redis_conf['port'],
            decode_responses=True)

    @lazy_start
    def set_key_value(self, **data):
        if data['session_id']:
            mapping = {k: v for k, v in data.items() if k != 'session_id'}
            self.redis.hset(name=data['session_id'], mapping=mapping)
        else:
            session_id = str(uuid.uuid4())
            mapping = {
                "user_id": f"user:{data['user_id']}:session",
                "cookie": data['cookie']
                }
            self.redis.hset(name=session_id, mapping=mapping)

    @lazy_start
    def get_values(self, cookie):
        pass
