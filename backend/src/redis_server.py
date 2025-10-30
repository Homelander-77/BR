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
    def set_key_value(self, **kwargs):
        data = dict()
        for name, value in kwargs:
            data[name] = value

        if data['session_id']:
            pass
        else:
            session_id = str(uuid.uuid4())
            self.redis.hset(name=data[''])

    @lazy_start
    def get_values(self, cookie):
        pass
