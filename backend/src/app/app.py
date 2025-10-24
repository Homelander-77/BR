import sys

from server import Server
from postgres import Database
from app.config import server_conf
from app.login import login
from app.registration import reg
from app.cookie_check import cookie_check
from app.recommendations import rec


if __name__ == "__main__":
    host = server_conf['host']
    port = server_conf['port']
    pg = Database()
    server = Server((host, port))
    try:
        server.add_path('/login', login)
        server.add_path('/reg', reg)
        server.add_path('/cookie', cookie_check)
        server.add_path('/rec', rec)
        server.start()
    except KeyboardInterrupt:
        pg.disconnect()
        sys.exit(0)
