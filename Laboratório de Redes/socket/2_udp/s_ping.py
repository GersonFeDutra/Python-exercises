#!/usr/bin/python3
'''
Ping Server
'''
from random import randint
from socket import AF_INET, SOCK_DGRAM, socket

IP = ''  # Default to localhost '127.0.0.1'
PORT = 50000  # Port to listen on (non-privieged ports are > 1023)
DATA_PAYLOAD: int = 1024  # The maximum amount of data to be received at once


def main() -> None:
    '''
    Starts a ping server that receive ping requests
    '''

    # Create UDP socket
    server_socket = socket(AF_INET, SOCK_DGRAM)

    # Bind the socket to the port
    server_address = (IP, PORT)
    print('\033[34m''Starting up ping server on %s port %s ''\033[m' %
          server_address)
    server_socket.bind(server_address)

    while True:
        # Gera números randômicos entre 0 to 10
        rand = randint(0, 10)

        # Recebe o pacote e o endereço do cliente
        message, address = server_socket.recvfrom(DATA_PAYLOAD)
        print('\033[35m' f'Log: received package from {address}' '\033[m')

        # Coloca a mensagem em maíusculo
        message = message.upper()

        # Se o número rand é menor que 4, consideramos o pacote perdido.
        if rand < 4:
            continue

        # Caso contrário, o servidor responde
        server_socket.sendto(message, address)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\033[31m' 'Process interrupted by the user.' '\033[m')
