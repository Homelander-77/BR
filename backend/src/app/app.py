import sys

from server import Server
from postgres import Database
from config import server_conf
from app.login import login, check_auth
from app.registration import reg
from app.recommendations import rec


if __name__ == "__main__":
    host = server_conf['host']
    port = server_conf['port']
    pg = Database()
    server = Server((host, port))
    try:
        server.add_path('/login', login)
        server.add_path('/reg', reg)
        server.add_path('/check_auth', check_auth)
        server.add_path('/rec', rec)
        server.start()
    except KeyboardInterrupt:
        pg.disconnect()
        sys.exit(0)
