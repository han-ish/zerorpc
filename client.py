from services import TcpDump, Server, Client
import time

tcpdumpObj = TcpDump()

# Initializing server and client
server = Server()
client = Client()

# Setting interface
tcpdumpObj.setinterface("lo")

# Starting trace
tcpdumpObj.start_trace()

# Starting server
server.start()
print("server starting here")

time.sleep(5)
# Starting client
print("client starting here")
client.start()

time.sleep(5)
# STopping server
server.stop()

tcpdumpObj.stop_trace()

