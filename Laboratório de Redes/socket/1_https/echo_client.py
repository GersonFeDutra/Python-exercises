import socket

HOST: str = '127.0.0.1'
PORT: int = 65432

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
CLIENT_ADDRESS = (HOST, PORT)
print('Connection to %s port %s' % CLIENT_ADDRESS)
sock.connect(CLIENT_ADDRESS)

# Send data
message = 'Hello World'
sock.sendall(message.encode())

DATA_PAYLOAD: int = 1024
data = sock.recv(DATA_PAYLOAD)
print(f'Received: {data}')

print('Closing connection to the server')
sock.close()
