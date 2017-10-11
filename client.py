from services import TcpDump, DummyServer
from servers import Server
from clients import Client
import time

tcpdumpObj = TcpDump()

# Initializing server and client
#server = Server()
server = DummyServer()
client = Client()

# Setting interface
tcpdumpObj.setinterface("lo")

# Starting trace
tcpdumpObj.start_trace()

# Starting dummy server
server.start()

# Client reading
time.sleep(1)
print("client reading here")
client.read()
time.sleep(5)
server.stop()
print("past that heh")
tcpdumpObj.stop_trace()

