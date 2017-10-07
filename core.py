import zerorpc 
import gevent
import subprocess


class TCPDump(object):
    """A bar class"""
    def __init__(self, handler):
        self.handler = handler

    def list(self):
        """This method will list the interfaces
        Usage : list"""
        self.interfaces = subprocess.Popen(['/usr/sbin/tcpdump', 
                                            '--list-interface'], 
                                           stdout=subprocess.PIPE)
        return self.interfaces.stdout.read().split('\n')
    
    def start_trace(self, interface):
        """This method will start a trace on the interface
        Usage : start_trace <interface>"""
        self.interface = interface
        print("tracing interface {}".format(interface))
        self.tcpdump = subprocess.Popen(['/usr/sbin/tcpdump', '-i', interface],
                                       stdout=subprocess.PIPE)

    def stop_trace(self):
        """This method will stop the trace
        Usage : stop_trace"""
        print("stopping trace on interface {}".format(self.interface))
        try:
            self.tcpdump.terminate()
            with self.tcpdump.stdout as stdout:
                #data = self.tcpdump.stdout.read()   # just for demo
                data = stdout.read()
            #with gevent.Timeout(3, False):
            #    data = self.tcpdump.stdout.read()
        except Exception as e:
            print("No trace started. Caught : {}".format(e))
        else:
            return data if data.strip() else "No data found"

    def halt (self):
        """This method will halt the service and the server
        Usage : halt"""
        print("processing halt request")
        try:
            gevent.spawn_later(1, self.handler.stop)
            #self.handler.stop()
        except Exception as e:
            return "nothing is listening {}".format(e)


class Handler(object):
    """This class handles the request for services"""
    def __init__(self, service):
        """This method initializes the service available"""
        self.port = 8888
        services = {'tcpdump' : {'serv' : TCPDump, 'port' : 8888}}
        print("service : ", service)
        if service not in services:
            raise ValueError("Service unavailable")
        server = services[service]['serv']
        self.port = services[service]['port']
        #self.server = zerorpc.Server(Bar(self))    # Initializing the server with the service
        self.server = zerorpc.Server(server(self))
        try:
            self.server.bind('tcp://0.0.0.0:{}'.format(self.port))
        except Exception as exc:
            print(exc)

    def getport(self):
        """This method returns the port running the service"""
        return self.port

    def run(self):
        """This method is used to run the zerorpc server for the requsted
        service"""
        print('serving on port {}'.format(self.port))
        self.server.run()

    def stop(self):
        """This methos is used to stop the zerorpc server running the service"""
        print("stopping server now. . . . .")
        self.server.stop()
        self.server.close()

