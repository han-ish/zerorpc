from services import TcpDump
import time

tcpdumpObj = TcpDump()
tcpdumpObj.setinterface("eth0")
tcpdumpObj.start_trace()
time.sleep(5)
tcpdumpObj.stop_trace()

