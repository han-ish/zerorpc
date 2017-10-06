import zerorpc 
import gevent

from tcpdumper import TCPDump

class Foo(object):
    """This is the main service class (Dummy)"""
    def __init__(self, handler):
        """We hook the handler here"""
        self.handler = handler

    def bar(self):
        """A dummy method for demo purpose"""
        return "bar"

    def halt(self):
        """The method is used to shutdown the server"""
        print("trying to stop")
        gevent.spawn_later(1, self.handler.stop)
        #self.handler.server.stop()
        #self.handler.server.close()

    def goof(self):
        """Another dummy method for demo purpose"""
        return "goof"

    def baz(self, msg):
        """Another dummy method. Usage : baz <msg>"""
        return "{} from server".format(msg)

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

