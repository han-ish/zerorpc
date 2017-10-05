from __future__ import print_function
from gevent.server import StreamServer
from foo import Handler, Foo

METHODS = [func for func in dir(Foo) if callable(getattr(Foo, func)) and not func.startswith('__')]
print(METHODS)



#SERVICES = [key.lower() for key,val in vars(zeroservices).items() if type(val) == type and key not in 'Handler']

def serv(socket, address):
    """This method handles the new connection from the clients"""
    print('New connection from %s:%s' % address)
    socket.sendall(','.join(METHODS))
    service = socket.recv(1024) # 'service' is the service requested by the client
    print("Client requesting service : {}".format(service))
    handler = Handler(service)  # calls the Handler class for handling the request
    port = handler.getport()    # requesting the port  for the service
    socket.sendall(str(port))   # sending the port to the client
    handler.run()   # calling the run method on the service handler
    socket.close()


if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 8000), serv)
    print('Starting echo server on port 8000')
    server.serve_forever()

