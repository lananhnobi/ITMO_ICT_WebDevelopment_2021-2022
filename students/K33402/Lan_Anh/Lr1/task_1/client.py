import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('Hello, server'.encode("UTF-8"))

data = sock.recv(1024)
sock.close()

print(data.decode("UTF-8"))