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



See remote service documentation
--------------------------------

You can introspect the remote service; it happens automatically if you don't
specify the name of the function you want to call::

   $ zerorpc --client --connect tcp://127.0.0.1:8000 # This line is required to start the generic server
   $ zerorpc tcp://127.0.0.1:8888
