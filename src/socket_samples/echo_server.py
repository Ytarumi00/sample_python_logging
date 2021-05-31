from socketserver import TCPServer, BaseRequestHandler, StreamRequestHandler
from time import sleep
import logging
import pickle

address = ('192.168.1.30', 5000)

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print("sleep 3")
        sleep(3)
        message = self.request.recv(4)
        print('receved')
        self.request.sendall(b'Reply: ' + message)


if __name__ == '__main__':
    TCPServer.allow_reuse_address = True  # avoid, OSError: [Errno 98] Address already in use

    with TCPServer(address, EchoHandler) as server:
        server.serve_forever()