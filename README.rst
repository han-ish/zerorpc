=====================
zerorpc-custom-server
=====================

The server handles requests from client that will spawn a new server with requested service and will return a port address for the client to connect to.



Installation
------------

On most systems, its a matter of::

  $ pip install zerorpc


Usage
-----

* server : 
    $ python server.py
* client :
    $ python client.py

More Usage
----------
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
self.sock.send("tcpdump")
service_port = self.sock.recv(1024)
tcpdump = zerorpc.Client('tcp://127.0.0.1:{}'.format(service_port))

* List interfaces available : 
        interfaces = tcpdump.list()
* Start trace on an interface
        tcpdump.set_trace(interface)    # Eg : tcpdump.set_trace("wlan0")
* Stop trace
        tcpdump.stop_trace()

..note::
        The services are pluggable as one wish in the core.py

