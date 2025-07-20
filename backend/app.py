import socket
import sys
import select

from parser import HTTPRequest
from response import MakeHTTPResponse
from psql import Database
from login import login
from registration import reg


class Server:
    def __init__(self, server_addr):

        self.server_addr = server_addr
        self.paths = {}
        self.sockets_list = []

    def start(self):
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.bind(self.server_addr)
        self.lsock.listen(5)
        self.sockets_list.append(self.lsock)
        print(f"Listening on {self.server_addr}")
        self.psql = Database()
        self.psql.start()
        print(self.psql.select())

        while True:
            read_sockets, _, _ = select.select(self.sockets_list, [], [])
            for notified_socket in read_sockets:
                if notified_socket == self.lsock:
                    conn, addr = self.lsock.accept()
                    print(f"Accepted new connection from \
                           module import symbol {addr}")
                    self.sockets_list.append(conn)
                else:
                    self.service_connection(notified_socket)

    def service_connection(self, conn):
        try:
            recv = conn.recv(1024)
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
                json, code = self.paths[request.path](request, self.psql)
                makeResponse = MakeHTTPResponse(code, json)
            else:
                makeResponse = MakeHTTPResponse(404, '')

            response = makeResponse.make()
            print(response.decode())
            while response:
                sent = conn.send(response)
                response = response[sent:]

        print("Close connection")
        self.sockets_list.remove(conn)
        conn.close()

    def add_path(self, path, func):
        self.paths[path] = func


if __name__ == "__main__":
    ip = '0.0.0.0'
    port = 8080
    server = Server((ip, port))
    try:
        server.add_path('/login', login)
        server.add_path('/reg', reg)
        server.start()
    except KeyboardInterrupt:
        sys.exit(0)
