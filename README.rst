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

server::

    $ python server.py

client::

    $ python client.py

More Usage
----------

.. code-block:: python

    from services import TcpDump
    import time

    tcpdumpObj = TcpDump()
    tcpdumpObj.setinterface("eth0")
    tcpdumpObj.start_trace()
    time.sleep(5)
    tcpdumpObj.stop_trace()
 
.. note::
        The services are pluggable as one wish in the core.py

