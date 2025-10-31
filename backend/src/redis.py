import threading
import redis

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
    def set_key_value(self, **data) -> None:
        mapping = {k: v for k, v in data.items() if k != 'session_id'}
        self.redis.hset(name=data['session_id'], mapping=mapping)

    @lazy_start
    def get_value(self, name, value) -> str:
        return str(self.redis.hget(name, value).decode())
