import socket

HOST: str = 'localhost'
PORT: int = 8083


def main(*_args) -> None:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    CLIENT_ADDRESS = (HOST, PORT)
    print('Connection to %s port %s' % CLIENT_ADDRESS)

    # Connect the socket to the server
    sock.connect(CLIENT_ADDRESS)

    sock.sendall('-t'.encode())

    DATA_PAYLOAD: int = 1024
    data = sock.recv(DATA_PAYLOAD)
    print(f'Time received: {data.decode()}')

    print('Closing connection to the server')
    sock.close()


if __name__ == '__main__':
    main()
