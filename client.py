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
        self.sock.send("tcpdump")
        service_port = self.sock.recv(1024)
        print("got : ", service_port)
        #cli = zerorpc.Client()
        tcpdump = zerorpc.Client('tcp://127.0.0.1:{}'.format(service_port))
        interfaces = tcpdump.list()
        for interface in interfaces:
            print(interface)

        iface = raw_input("Enter the interface : ")
        tcpdump.start_trace(iface)
        time.sleep(5)
        #for interface in cli.list():
        #    print(interface)
        res = tcpdump.stop_trace()
        print("Response : {}".format(res))
        tcpdump.halt()
        tcpdump.close()

if __name__ == '__main__':
    client = Client(8000)
    client.run()

