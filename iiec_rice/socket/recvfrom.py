import socket

# use ipv4 net address family
afn = socket.AF_INET
#use udp
myp = socket.SOCK_DGRAM

s = socket.socket( afn, myp )

ip = "192.168.0.12"
port = 1234

s.bind( (ip,port) )

x = s.recvfrom(1024)
print(x)
