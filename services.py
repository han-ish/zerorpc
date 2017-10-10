import zerorpc
import socket

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

