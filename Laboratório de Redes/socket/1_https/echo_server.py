import socket

HOST: str = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT: int = 65432  # Port to listen on (non-privieged ports are > 1023)
DATA_PAYLOAD: int = 1024  # The maximum amount of data to be received at once

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
SERVER_ADDRESS = (HOST, PORT)
print('\033[34m''Starting up echo server on %s port %s''\033[m' %
      SERVER_ADDRESS)
sock.bind(SERVER_ADDRESS)

MAX_QUEUE_CONNECT: int = 7  # specifies the max no, of queued connections
sock.listen(MAX_QUEUE_CONNECT)  # Listen to clients
client, adress = sock.accept()

while True:
    print('Waiting to receive a message from client...')
    data = client.recv(DATA_PAYLOAD)
    message = data.decode()

    if message:
        print(f'Data: {message}')
        client.sendall(message.encode())
    else:
        break

print('Closing client connection', client)
client.close()
