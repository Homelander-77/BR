import psycopg2
import psql_config


class Database:
    def __init__(self):
        self.conn = None
        self.cur = None

    def start(self):
        self.conn = psycopg2.connect(
            dbname=psql_config.param['dbname'],
            user=psql_config.param['user'],
            password=psql_config.param['password'],
            host=psql_config.param['host'],
            port=psql_config.param['port'])
        self.cur = self.conn.cursor()

    def stop(self):
        self.cur.close()
        self.conn.close()

    def get_password_by_login(self, login):
        self.cur.execute(f'select password from login_password where login={login}')
        ans = self.cur.fetchone()
        return ans[0]
    
    def add_user(self, firstname, lastname, login, password):
        self.cur.callproc("add_user", (firstname, lastname, login, password))
        ans = self.cur.fetchone()
        self.conn.commit()
        return ans[0]


