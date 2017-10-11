import socket

class Client(object):
    """This class is a wrapper for dummy clients"""
    def __init__(self, port):
        self.host, self.port  = '127.0.0.1', port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def read(self):
        """This methods reads the message from client"""
        print("connecting to server in port {}".format(self.port))
        self.sock.connect((self.host, self.port))
        self.sock.send("hello world")
        msg = self.sock.recv(1024)
        self.sock.close()
        print("message was {}".format(msg))
        return msg

if __name__ == '__main__':
    client = Client(9999)
    client.read()

