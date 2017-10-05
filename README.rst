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


Call the server from the command-line
-------------------------------------

Now, in another terminal, call the exposed module::

  $ zerorpc --client --connect tcp://127.0.0.1:8000 # This line is required to start the generic server
  $ zerorpc --client --connect tcp://127.0.0.1:8888


See remote service documentation
--------------------------------

You can introspect the remote service; it happens automatically if you don't
specify the name of the function you want to call::

   $ zerorpc --client --connect tcp://127.0.0.1:8000 # This line is required to start the generic server
  $ zerorpc tcp://127.0.0.1:8888
  Connecting to "tcp://127.0.0.1:1234"
  [Foo]
   goof Another dummy method for demo purpose
   bar  A dummy method for demo purpose
   halt The method is used to shutdown the server
   baz  Another dummy method. Usage : baz <msg>

