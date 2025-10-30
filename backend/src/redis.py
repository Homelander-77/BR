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
        redis = None

    def connect(self):
        redis = redis.Redis(host=redis_conf['host'], \
            port=redis_conf['port'], \
            decode_responses=True)

    def set_key_value(self, **kwargs):
        pass

    @lazy_start
    def get_session_id(self, cookie):
        pass
