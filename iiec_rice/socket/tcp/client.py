import socket

s = socket.socket()

serverip = "192.168.122.223"
serverport = 2222

s.connect( (serverip, serverport) )

print(s.recv(100))
s.send(b"i'm client1")

