import zerorpc
import socket

class Client(object):
    def __init__(self, port):
        """The client get initialized here"""
        self.host, self.port  = '127.0.0.1', port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def run(self):
        services = self.sock.recv(1024)
        print(services)
        self.sock.send("foo")
        service_port = self.sock.recv(1024)
	print("got : ", service_port)
        cli = zerorpc.Client()
        cli.connect('tcp://127.0.0.1:{}'.format(service_port))
        response = cli.bar()
        print(response)
        res = cli.goof()
        print(res)
        cli.halt()

if __name__ == '__main__':
    client = Client(8000)
    client.run()

