import psycopg2
import json
import threading

from .config import db_conf


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
            dbname=db_conf['db_name'],
            user=db_conf['user'],
            password=db_conf['password'],
            host=db_conf['host'],
            port=db_conf['port'])
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.cur.close()
        self.conn.close()

    def get_password_by_login(self, login):
        self.cur.callproc("get_password_by_login", (login, ))
        ans = self.cur.fetchone()
        return ans[0]

    def get_salt_by_login(self, login):
        self.cur.callproc("get_salt_by_login", (login, ))
        ans = self.cur.fetchone()
        return ans[0]

    def add_user(self, firstname, lastname, login, password, salt, cookie):
        self.cur.callproc("add_user", (firstname, lastname, login, password, \
                                       salt, cookie['id'], cookie['expire']))
        ans = self.cur.fetchone()
        self.conn.commit()
        return ans[0]

    def add_cookie(self, login, cookie):
        self.cur.callproc("set_cookie", (login, cookie['id'], cookie['expire']))
        self.conn.commit()

    def get_cookie_expire(self, cookie):
        self.cur.callproc("get_cookie_expire", (cookie,))
        ans = self.cur.fetchone()
        return ans[0]

    def get_rec(self):
        self.cur.callproc('get_recommendations', ())
        ans = self.cur.fetchall()
        return json.loads(json.dumps(ans))[0][0]
