import socket

s = socket.socket()         # socket.socket('type of address | ipv4 or ipv6', 'type of connection | Tcp or Udp), default is ipv4 and tcp

print('Scoket Created')

s.bind(('localhost', 9999))

s.listen(3)     # it will listen for 3 clients

print('waiting for the connections')

while True:
    c_socket, c_address = s.accept()
    name = c_socket.recv(1024).decode()
    print("Connected with", c_address, name)

    
    c_socket.send(bytes('welcome to server', 'utf-8'))

    c_socket.close()