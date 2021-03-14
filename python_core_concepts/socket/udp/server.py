import socket
import os
import time
import threading

srcip = "192.168.0.12"
dstip = "192.168.0.14"
srcport = 1234
dstport = 4321

#multithread recive functions
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((srcip, srcport))

def a():
  while True:
    x = s.recvfrom(10)
    clientip = x[1][0]
    data = x[0].decode()
    print(x)
    time.sleep(5)
    #print( os.system(data) )

def b():
  while True:
    x = s.recvfrom(10)
    clientip = x[1][0]
    data = x[0].decode()
    print(x)
    time.sleep(5)
    #print( os.system(data) )

x1 = threading.Thread ( target=a )
x2 = threading.Thread ( target=b )

x1.start()
x2.start()

#send function
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def c():
  while True:
    ms = input("You message:")
    data = ms.encode()
    s2.sendto(data, (dstip, dstport))

x3 = threading.Thread( target=c )
x3.start()


