import socket
from time import sleep


port_input = input("Введите номер порта для сервера -> ")
ip_input = input("Введите IP для сервера -> ")

sock = socket.socket()
sock.setblocking(1)
sock.connect((ip_input, int(port_input)))

msg = input()
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
