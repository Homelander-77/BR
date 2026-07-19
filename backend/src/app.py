import sys

from server import Server
from db.postgres import Database
from config import server_conf
from routes.login import login, check_auth
from routes.registration import reg
from routes.recommendations import rec


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
