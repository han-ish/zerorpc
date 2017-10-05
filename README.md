Zerorpc Custom Service
------------------------

The server handles requests from client that will spawn a new server with requested service and will return a port address for
 the client to connect to.

### Prerequisites

zerorpc

### Installation

pip install zerorpc

### Usage

server
-------

python server.py

client
------

# Any client socket will do

import socket
import zerorpc

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
# This will get the available services
services = self.sock.recv(1024)
print(services)
sock.send("foo")
service_port = sock.recv(1024)
client = zerorpc.Client()
client.connect('tcp://127.0.0.1:{}'.format(service_port))
response = client.bar()
print(response)
res = client.goof()
print(res)
client.halt()


##### Cmdline Usage

# start the server first
python server.py

# Now connect the zerorpc client
zerorpc --client tcp://127.0.0.1:8000 # This step is required since we're running the generic server using python too

# Now we can use the services
zerorpc --client tcp://127.0.0.1:8888 # This will list all the available service using cmdline

Eg :- zerorpc --client tcp://127.0.0.1:8888 bar



More usage details
------------------
# start the server
python server.py

# client side usage
C:\Users\user\python\zero>zerorpc --client tcp://127.0.0.1:8888
connecting to "tcp://127.0.0.1:8888"
[Foo]
goof Another dummy method for demo purpose
bar  A dummy method for demo purpose
halt The method is used to shutdown the server
baz  Another dummy method. Usage : baz <msg>


C:\Users\user\python\zero>zerorpc --client tcp://127.0.0.1:8888 bar
connecting to "tcp://127.0.0.1:8888"
'bar'

C:\Users\user\python\zero>zerorpc --client tcp://127.0.0.1:8888 baz "hello world"
connecting to "tcp://127.0.0.1:8888"
'hello world from server'

C:\Users\user\python\zero>zerorpc --client tcp://127.0.0.1:8888 halt
connecting to "tcp://127.0.0.1:8888"
Traceback (most recent call last):
......
zerorpc.exceptions.TimeoutExpired: timeout after 30s, when calling remote method halt

# Just to prove the server closed the service

C:\Users\user\python\zero>telnet 127.0.0.1 8888
Connecting To 127.0.0.1...Could not open connection to the host, on port 8888: Connect failed

