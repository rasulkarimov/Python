import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect(("192.168.0.12" , 1234))
s.send(b"hi")
s.recv(1024)
s.close()
