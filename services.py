import zerorpc
import socket
import subprocess

class TcpDump(object):
    """The TCPDump service"""
    def __init__(self):
        self.interface = 'lo'   # default listening interface
        # we know the host and the port address of the generic server
        self.host, self.port  = '127.0.0.1', 8000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self._setup()

    def _setup(self):
        """This method sets up the required connections"""
        self.sock.send("tcpdump")
        service_port = self.sock.recv(1024)
        self.tcpdump = zerorpc.Client('tcp://127.0.0.1:{}'.format(service_port))

    def setinterface(self, interface):
        """This method sets the interface that is to listen"""
        self.interface = interface

    def start_trace(self):
        """This method starts the trace"""
        self.tcpdump.start_trace(self.interface)

    def stop_trace(self):
        """This method stops the current trace"""
        self.tcpdump.stop_trace()


class Server(object):
    """A wrapper for server app"""
    def __init__(self):
        self.args = ["python", 'serv_app.py']

    def start(self):
        self.server = subprocess.Popen(self.args, stdout=subprocess.PIPE)

    def stop(self):
        self.server.terminate()

class Client(object):
    """A wrapper for client app"""
    def __init__(self):
         self.args = ["python", 'client_app.py']

    def start(self):
        self.server = subprocess.Popen(self.args, stdout=subprocess.PIPE)

    def stop(self):
        self.server.terminate()

