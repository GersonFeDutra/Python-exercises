#!/usr/bin/python3
'''
Ping Server
'''
from socket import AF_INET, SOCK_DGRAM, socket

IP = ''  # Default to localhost '127.0.0.1'
PORT = 40000  # Port to listen on (non-privieged ports are > 1023)
DATA_PAYLOAD: int = 1024  # The maximum amount of data to be received at once


def main() -> None:
    ''' Listens to "ping" requests '''
    # Create UDP socket
    server_socket = socket(AF_INET, SOCK_DGRAM)

    # Bind the socket to the port
    SERVER_ADDRESS = (IP, PORT)
    print('\033[35m''Starting up ping server on %s port %s...''\033[m' %
          SERVER_ADDRESS)
    server_socket.bind(SERVER_ADDRESS)

    while True:
        # Recebe o pacote e o endereço do cliente
        message, address = server_socket.recvfrom(DATA_PAYLOAD)
        print('\033[33m\t' f'Log: received package from {address}' '\033[m')

        # Coloca a mensagem em verde e maíúsculo
        message = f'\033[35m{message.decode().upper()}\033[m'.encode()

        # Caso contrário, o servidor responde
        server_socket.sendto(message, address)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\033[31m''Process interrupted by user.''\033[m')
