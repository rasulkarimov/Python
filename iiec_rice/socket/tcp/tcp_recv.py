import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ip = "192.168.0.12"
port = 1234

s.bind( (ip, port) )

s.listen()

# any sender connect -> memorice -> maintain connection
c , addr = s.accept()

x = c.recv(1024)
print(x)

s.send(b"acccepted")

