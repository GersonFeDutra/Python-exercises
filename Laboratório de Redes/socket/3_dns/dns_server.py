#!/usr/bin/python3
'''
Server DNS
'''
import socket
from sys import stderr


def log(*args, **kwargs) -> None:
    '''Log a message to stderr'''
    print('\033[33m\t', end='Log: ', flush=True)
    print(*args, **kwargs, file=stderr)
    print(end='\033[m', flush=True)


IP: str = ''  # Default to localhost
PORT: int = 1234
DATA_PAYLOAD: int = 4096

# Table with DNS info
# Each key-value pair contains a host name and a corresponding IP address
dns_table: dict[str, str] = {
    'alice.com': '127.0.0.1',
    'google.com': '8.8.8.8',
    'twitter.com': '199.16.156.0',
    'instagram.com': '104.244.42.129',
}


def main() -> None:
    '''
    Starts the DNS server
    '''
    # Creates an UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Associates the socket to the port
    SERVER_ADDRESS = (IP, PORT)
    sock.bind(SERVER_ADDRESS)

    print('\033[35m' f'DNS server running at port {PORT}...' '\033[m')

    while True:
        # Aguarde por uma requisição do cliente
        data, address = sock.recvfrom(DATA_PAYLOAD)
        name: str = data.decode()
        log(f'Received "\033[m{name}\033[33m" from {address}')

        # Procure pelo nome de host na tabela DNS
        ip_address: str | None = dns_table.get(data.decode(), None)

        if ip_address is None:
            # If name not found on table, return eror message
            message = '\033[31m' + 'Unknow host name' + '\033[m'
        else:
            # Else, return the corresponing address
            message = ip_address

        log(f'sent "\033[m{message}\033[32m"')

        # Sends the response to the client
        sock.sendto(message.encode(), address)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\033[31m' 'Process interrupted by user.' '\033[m')
