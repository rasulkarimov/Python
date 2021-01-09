import socket
import threading
import time

srcip = "192.168.0.14"
srcport = 4321
dstip = "192.168.0.12"
dstport = 1234

#send function
s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
def a():
  while True:
    cm = input("Type command:")
    data = cm.encode()
    s.sendto(data, (dstip, dstport))

# recive function
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2.bind((srcip, srcport))
def b():
  while True:
    x = s2.recvfrom(10)
    print(x)
    time.sleep(60)
    
x1 = threading.Thread( target=a )
x2 = threading.Thread( target=b )
x2.start()
x1.start()

