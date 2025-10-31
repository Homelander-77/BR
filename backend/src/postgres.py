import psycopg2
import threading

from config import db_conf
from lazy_start import lazy_start


class Database:
    __instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls.__instance is None:
                cls.__instance = super(Database, cls).__new__(cls)
            return cls.__instance

    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = psycopg2.connect(
            dbname=db_conf['name'],
            user=db_conf['user'],
            password=db_conf['password'],
            host=db_conf['host'],
            port=db_conf['port'])
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.cur.close()
        self.conn.close()

    @lazy_start
    def execute_func(self, func, *args):
        self.cur.callproc(func, *args)
        ans = self.cur.fetchall()
        return ans if len(ans) > 1 else ans[0]
