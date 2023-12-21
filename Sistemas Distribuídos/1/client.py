"""Client."""
from socket import socket, AF_INET, SOCK_STREAM

PKG_SIZE: int = 1024
HOST: str = 'localhost'
PORT: str = '1234'

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT, ))  # Connect to server (block until accepted)
s.send('Hello World!')  # Send some data
data = s.recv(PKG_SIZE)  # Receive the response

print(data)
s.close()
