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
PORT: int = 8082  # Port to listen on (non-privieged ports are > 1023)
DATA_PAYLOAD: int = 1024  # The maximum amount of data to be received at once

def res(data: bytes, address):
    
    print(f'Received message from client {address}')
    message = data.decode()

    if message == '-t':
        print(f'Sending current time... to {address}')

        new_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = str(time.strftime("%H:%M:%S", time.localtime())).encode()
        new_sock.sendto(message, address)
    else:
        print('Error: Invalid request')

def main(*_args) -> None:
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    SERVER_ADDRESS = (HOST, PORT)
    print('\033[34m''Starting up echo server on %s port %s''\033[m' %
        SERVER_ADDRESS)

    sock.bind(SERVER_ADDRESS)

    while True:
        pei = sock.recvfrom(DATA_PAYLOAD)
        Thread(target=res, args=pei)\
            .start()


if __name__ == '__main__':
    main()
