import psycopg2
import psql_config
import json


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

    def get_rec(self):
        self.cur.callproc('get_recommendations', ())
        ans = self.cur.fetchall()
        return json.loads(ans)


psql = Database()
psql.start()
print(psql.get_rec())
