import socket
import select
import http
import signal
import errno

from config import server_conf
from utils.HTTPResponse import HTTPResponse
from utils.HTTPRequest import HTTPRequest
from app.logger_manager import main_logger, general_logger


class Server:
    def __init__(self, server_addr):
        self.server_addr = server_addr
        self.paths = {}
        self.sockets_list = []
        self.stop = False

    def start(self):
        signal.signal(signal.SIGINT, lambda s, f: self.request_shutdown())

        try:
            self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.lsock.bind(self.server_addr)
            self.lsock.listen(server_conf['max_con'])
            self.sockets_list.append(self.lsock)
            general_logger.info("Server started")
            main_logger["server"].info(f"Listening on {self.server_addr}")
        except OSError as exc:
            if exc.errno == errno.EADDRINUSE:
                main_logger["server"].error(
                    f"Address {self.server_addr} already used: {exc}")
            elif exc.errno == errno.EACCES:
                main_logger["server"](
                    f"Permission denied on {self.server_addr}: {exc}"
                )
            else:
                main_logger["server"](
                    f"Socket setup failed on {self.server_addr}: {exc}"
                )
        while not self.stop:
            read_sockets, _, _ = select.select(self.sockets_list, [], [], 1)
            for notified_socket in read_sockets:
                if notified_socket == self.lsock:
                    conn, addr = self.lsock.accept()
                    general_logger.logger(f"Accepted new connection {addr}")
                    main_logger["server"].info(
                        """Accepted new connection
                        from module import symbol {addr}""")
                    
                    self.sockets_list.append(conn)
                else:
                    try:
                        self.service_connection(notified_socket)
                    except Exception as exc:
                        main_logger["server"].error(
                            f"""Error servicing connection
                             {notified_socket}: {exc}""")
                        self.stop = True
        else:
            self._close_all()

    def request_shutdown(self):
        general_logger.info("Stutdown server")
        main_logger["server"].info("Stutdown")
        self.stop = True

    def _close_all(self):
        for sock in self.sockets_list:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        main_logger["server"].info("Closed all sockets")

    def service_connection(self, conn):
        try:
            recv = conn.recv(server_conf['rec_mes'])
            message = recv

            if not message:
                general_logger["server"].info("Data missing")
                self.sockets_list.remove(conn)
                conn.close()
                return ''

            while b'\r\n\r\n' not in message:
                recv = conn.recv(1024)
                message += recv

        except ConnectionResetError:
            general_logger["server"].error(
                "Close connection because of ConnectionResetError")
            self.sockets_list.remove(conn)
            conn.close()
            return ''

        if message:
            request = HTTPRequest(message.decode())

            if request.path in self.paths.keys():
                response = self.paths[request.path](request)
            else:
                response = HTTPResponse(http.HTTPStatus.NOT_FOUND, '').make(cookie=False)

            while response:
                sent = conn.send(response)
                response = response[sent:]

        general_logger.info("Close connection")
        main_logger.info("Close connection")
        self.sockets_list.remove(conn)
        conn.close()

    def add_path(self, path, func):
        self.paths[path] = func
