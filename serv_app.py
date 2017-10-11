from __future__ import print_function
from gevent.server import StreamServer
from core import Handler

def serv(socket, address):
    """This method handles the new connection from the clients"""
    print('New connection from %s:%s' % address)
    service = socket.recv(1024) # 'service' is the service requested by the client
    socket.sendall("hello universe")   # sending the port to the client
    socket.close()


if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 9999), serv)
    print('Starting echo server on port 9999')
    server.serve_forever()

