import socket
import threading

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip = "0.0.0.0"
port = 2222

s.bind( (ip, port) )

s.listen()

def a(csession, addr):
    print(addr)
    csession.send(b"I'n server")
    data = csession.recv(100)
    print(data)

while True:
    csession, addr = s.accept()
    p = threading.Thread(target=a, args=(csession, addr))
    p.start()
