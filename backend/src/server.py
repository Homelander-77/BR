import socket
import select
import http
import signal

from app.config import server_conf
from utils.response import MakeHTTPResponse
from utils.HTTPRequest import ParseHTTPRequest


class Server:
    def __init__(self, server_addr):
        self.server_addr = server_addr
        self.paths = {}
        self.sockets_list = []
        self.stop = False

    def start(self):
        signal.signal(signal.SIGINT, lambda s, f: self.request_shutdown())

        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.bind(self.server_addr)
        self.lsock.listen(server_conf['max_con'])
        self.sockets_list.append(self.lsock)
        print(f"Listening on {self.server_addr}")

        while not self.stop:
            print(self.stop)
            read_sockets, _, _ = select.select(self.sockets_list, [], [], 1)
            for notified_socket in read_sockets:
                if notified_socket == self.lsock:
                    conn, addr = self.lsock.accept()
                    print(f"Accepted new connection from \
                           module import symbol {addr}")
                    self.sockets_list.append(conn)
                else:
                    self.service_connection(notified_socket)
        else:
            self._close_all()

    def request_shutdown(self):
        print(" Shutdown requests")
        self.stop = True

    def _close_all(self):
        for sock in self.sockets_list:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        print("All sockets closed")

    def service_connection(self, conn):
        try:
            recv = conn.recv(server_conf['rec_mes'])
            message = recv

            if not message:
                print("Close connection, no data")
                self.sockets_list.remove(conn)
                conn.close()
                return ''

            while b'\r\n\r\n' not in message:
                recv = conn.recv(1024)
                message += recv

        except ConnectionResetError:
            print("Close connection because of ConnectionResetError")
            self.sockets_list.remove(conn)
            conn.close()
            return ''

        if message:
            request = HTTPRequest(message.decode())

            if request.path in self.paths.keys():
                response = self.paths[request.path](request)
            else:
                makeResponse = MakeHTTPResponse(http.HTTPStatus.NOT_FOUND, '')
                response = makeResponse.make(cookie=False)

            print(response.decode())
            while response:
                sent = conn.send(response)
                response = response[sent:]

        print("Close connection")
        self.sockets_list.remove(conn)
        conn.close()

    def add_path(self, path, func):
        self.paths[path] = func
