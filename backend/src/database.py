import psycopg2
import threading
import sys

from config import db_conf
from lazy_start import lazy_start
from app.logger_manager import general_logger, main_logger


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
        try:
            self.conn = psycopg2.connect(
                dbname=db_conf['name'],
                user=db_conf['user'],
                password=db_conf['password'],
                host=db_conf['host'],
                port=db_conf['port'])
        except psycopg2.OperationalError as error:
            general_logger.error("Error with database connection")
            main_logger["database"].error(error)
            sys.exit(0)
        general_logger.info("Connect to database")
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.cur.close()
        self.conn.close()

    @lazy_start
    def execute_func(self, func, *args):
        try:
            self.cur.callproc(func, args)
        except psycopg2.OperationalError:
            main_logger["database"].error()
            return 0
        row = self.cur.fetchall()[0]
        if "add" in func:
            self.conn.commit()
        if not row:
            return 0
        return row[0] if len(row) == 1 else row
