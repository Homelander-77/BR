import threading
import redis

from lazy_start import lazy_start
from config import redis_conf
from app.logger_manager import LoggerManager as L


class Redis:
    __instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls.__instance is None:
                cls.__instance = super(Redis, cls).__new__(cls)
            return cls.__instance

    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = redis.Redis(
                host=redis_conf['host'],
                port=redis_conf['port'],
                decode_responses=True)
            if self.conn.ping():
                L.main_logger["redis"].info(
                    f"Connected to {redis_conf['host']}:{redis_conf['port']}")
                L.general_logger.info("Connected to redis")

        except redis.ConnectionError:
            L.main_logger["redis"].error(
                f"Connection lost {redis_conf['host']}:{redis_conf['port']}")
            L.general_logger.error("Failed to connect redis")

    def disconnect(self):
        self.conn.close()
        self.conn.connection_pool.disconnect()

    @lazy_start
    def set_key_value(self, data: dict) -> None:
        mapping = {k: v for k, v in data.items() if k != 'session_id'}
        self.conn.hset(name=data['session_id'], mapping=mapping)

    @lazy_start
    def get_value(self, name, value) -> str:
        return str(self.conn.hget(name, value))
