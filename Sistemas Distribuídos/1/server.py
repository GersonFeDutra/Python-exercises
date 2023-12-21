"""Server."""
from socket import socket, AF_INET, SOCK_STREAM

PKG_SIZE: int = 1024

s = socket(AF_INET, SOCK_STREAM)
connection, address = s.accept()

while True:
    data = connection.recv(PKG_SIZE)
    if not data:
        break
    connection.send(str(data) + '*')  # Return sent data with a *

connection.close()
