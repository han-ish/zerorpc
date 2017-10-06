import zerorpc
import socket
import time # just for delaying

class Client(object):
    def __init__(self, port):
        """The client get initialized here"""
        self.host, self.port  = '127.0.0.1', port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def run(self):
        self.sock.send("bar")
        service_port = self.sock.recv(1024)
        print("got : ", service_port)
        cli = zerorpc.Client()
        cli.connect('tcp://127.0.0.1:{}'.format(service_port))
        interfaces = cli.list()
        for interface in interfaces:
            print(interface)

        iface = raw_input("Enter the interface : ")
        cli.trace(iface)
        time.sleep(3)
        #for interface in cli.list():
        #    print(interface)
        response = cli.halt()
        print("got response here : {}".format(response))
        
if __name__ == '__main__':
    client = Client(8000)
    client.run()

