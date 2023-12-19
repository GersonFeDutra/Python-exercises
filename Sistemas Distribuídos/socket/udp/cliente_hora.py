import socket

HOST: str = 'localhost'
PORT: int = 8082
DATA_PAYLOAD: int = 1024

def main(*_args) -> None:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f'Sending message to {HOST} port {PORT}')

    sock.sendto('-t'.encode(), (HOST, PORT))

    while True:
        data, address = sock.recvfrom(DATA_PAYLOAD)
        print(f'Time received: {data.decode()}')
        break


if __name__ == '__main__':
    main()
