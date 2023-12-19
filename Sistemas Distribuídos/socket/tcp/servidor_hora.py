"""
1) Escreva um programa em Python, modelo cliente/servidor, com sockets TCP.
- O servidor deve atender um único pedido do cliente: Retornar o horário do momento solicitado.
- O cliente deve solicitar o horário ao servidor e encerrar. 
- O servidor deve ser multithread. 
2) Faça o mesmo para sockets UDP.

Utilize como base:
<https://github.com/rafaelperazzo/cc0026/blob/master/sockets/servidor_multithread.py>
<https://github.com/rafaelperazzo/cc0026/blob/master/sockets/cliente_multithread.py>
"""
import socket
import time
from threading import Thread

HOST: str = 'localhost'  # Standard loopback interface address (127.0.0.1)
PORT: int = 8083  # Port to listen on (non-privieged ports are > 1023)
DATA_PAYLOAD: int = 1024  # The maximum amount of data to be received at once

def response(client: socket.socket, address):
    print('Waiting to receive a message from client...')
    data = client.recv(DATA_PAYLOAD)
    message = data.decode()

    if message == '-t':
        print(f'Sending current time... to {address}')
        client.sendall(f'{time.strftime("%H:%M:%S", time.localtime())}'.encode())
    else:
        print('Error: Invalid request')

    print('Closing client connection', address)
    client.close()

def main(*_args) -> None:
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    SERVER_ADDRESS = (HOST, PORT)
    print('\033[34m''Starting up echo server on %s port %s''\033[m' %
        SERVER_ADDRESS)

    sock.bind(SERVER_ADDRESS)

    MAX_QUEUE_CONNECT: int = 10  # specifies the max no, of queued connections
    sock.listen(MAX_QUEUE_CONNECT)  # Listen to clients

    while True:
        client, address = sock.accept()
        thread = Thread(target=response, args=(client, address))\
                    .start()


if __name__ == '__main__':
    main()
