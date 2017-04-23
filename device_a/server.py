import os
import pickle
import sync_files
from socket import *
host = ""
port = 13000
buf = 1024008
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    hh = pickle.loads(data)
    print(hh)
    print(type(hh))
    updated = sync_files.find_updated_result(hh)
    print(updated)
    updated = pickle.dumps(updated)
    UDPSock.sendto(updated,addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)
