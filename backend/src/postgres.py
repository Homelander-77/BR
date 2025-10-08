import psycopg2
import pg_config
import json


class Database:
    def __init__(self):
        self.conn = None
        self.cur = None

    def start(self):
        self.conn = psycopg2.connect(
            dbname=pg_config.param['db_name'],
            user=pg_config.param['db_user'],
            password=pg_config.param['db_password'],
            host=pg_config.param['db_host'],
            port=pg_config.param['db_port'])
        self.cur = self.conn.cursor()

    def stop(self):
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
