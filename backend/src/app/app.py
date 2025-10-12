import sys

from .server import Server
from .postgres import Database
from .config import conf
from .login import login
from .registration import reg
from .cookie_check import cookie_check
from .recommendations import rec


if __name__ == "__main__":
    host = conf['server_host']
    port = conf['server_port']
    pg = Database()
    server = Server((host, port), pg)
    try:
        server.add_path('/login', login)
        server.add_path('/reg', reg)
        server.add_path('/cookie', cookie_check)
        server.add_path('/rec', rec)
        server.start()
    except KeyboardInterrupt:
        sys.exit(0)
