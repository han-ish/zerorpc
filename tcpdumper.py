import zerorpc 
import subprocess
import gevent

class Bar(object):
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
    
    def trace(self, interface):
        """This method will start a trace on the interface
        Usage : trace <interface>"""
        print("tracing interface {}".format(interface))
        self.tcpdump = subprocess.Popen(['/usr/sbin/tcpdump', '-i', 'lo'],
                                       stdout=subprocess.PIPE)
         
    def halt(self):
        """This method will halt the service and the server
        Usage : halt"""
        print("processing halt request")
        try:
            self.tcpdump.terminate()
            data = self.tcpdump.stdout.read()
            gevent.spawn_later(1, self.handler.stop)
        except Exception as e:
            return "nothing is listening {}".format(e)
        else:
            #gevent.spawn_later(5, self.handler.stop)
            return data

if __name__ == '__main__':
    server =  zerorpc.Server(Bar())
    server.bind("tcp://0.0.0.0:8000")
    server.run()

