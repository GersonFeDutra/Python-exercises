#!/usr/bin/python3
'''
Client DNS

Can search for names at the DNS server
Will be used to ping the server with the query alice.com
'''
from socket import AF_INET, SOCK_DGRAM, socket, timeout
from sys import argv, stderr
from time import time
from ipaddress import ip_address

DNS_IP: str = '127.0.0.1'  # Connect to localhost
DNS_PORT: int = 1234  # DNS server port
DNS_SERVER_ADDRESS = (DNS_IP, DNS_PORT)  # DNS server configuration

ALICE_HOST_NAME: str = 'alice.com'  # Connect to localhost
ALICE_PORT: int = 40000  # Server port

# Creates an UDP socket
CLIENT_SOCKET = socket(AF_INET, SOCK_DGRAM)


def dns_ask_ip(host_name: str, data_payload: int = 4096) -> str:
    '''Asks an IP to the DNS server
    @param:
        host_name: name of the server to search to
        data_payload: maximum amount of data to be received at once
    '''

    CLIENT_SOCKET.sendto(host_name.encode(), DNS_SERVER_ADDRESS)

    # Desailita o timeout temporariamente
    _t: float | None = CLIENT_SOCKET.gettimeout()
    CLIENT_SOCKET.settimeout(None)

    # Waits DNS server response
    data, _address = CLIENT_SOCKET.recvfrom(data_payload)

    CLIENT_SOCKET.settimeout(_t)
    return data.decode()


def push_warn(*args, **kwargs) -> None:
    '''print a warning at stderr'''
    print(end='\033[32m', flush=True)
    print(*args, file=stderr, **kwargs)
    print(end='\033[m', flush=True)


def push_error(*args, **kwargs) -> None:
    '''print an error at stderr'''
    print(end='\033[32m', flush=True)
    print(*args, file=stderr, **kwargs)
    print(end='\033[m', flush=True)


def ping(server_address: tuple[str, int], data_payload: int = 1024) -> None:
    '''
    Send a ping to he server.
    @param:
        server_address: server to ping to.
        time_limit: time to timeout.
        data_payload: maximum amount of data to be received at once
    '''
    message = 'Ping'
    start_time = time()  # (s) Used to account the ping shipping time

    print(f'Request: "{message}"')
    message = message.encode()
    CLIENT_SOCKET.sendto(message, server_address)

    try:
        response, server = CLIENT_SOCKET.recvfrom(data_payload)

        # Time taken for the message
        end_time: float = time() - start_time
        print(f'\033[36mReceived "\033[m{response.decode()}\033[36m" '
              f'from {server} in {end_time * 1000:.3f}ms')
    except timeout:
        push_warn('Ping request timed out')

    CLIENT_SOCKET.close()


def main(query: str = '', time_limit: int = 0, *_args) -> None:
    '''
    Searchs for IP at DNS server, or ping alice.com
    Ping alice.com
    @args:
        query: a query for search at the DNS,
               if none will search and ping alice.com instead.
        time_limit: time to timeout, non-positive value fallbacks to default.
    '''
    if time_limit <= 0:
        time_limit = 3

    if query:
        # Ask user to any host query to search at DNS server
        response: str = dns_ask_ip(query)

        try:
            ip_address(response)
            print('\033[32m' f'Ip adress of {query} is {response}' '\033[m')
        except ValueError:
            print('\033[33m' f'Received message: {response}' '\033[m')
    else:
        # Set time limit (sec)
        CLIENT_SOCKET.settimeout(time_limit)

        alice_ip: str = dns_ask_ip(ALICE_HOST_NAME)
        alice_server_address = (alice_ip, ALICE_PORT)  # Server configuration

        try:
            ip_address(alice_ip)
            print('\033[32m' f'Ip adress of {ALICE_HOST_NAME} is '
                  f'{alice_ip}\033[m')
            print(alice_ip)
            ping(alice_server_address)
        except ValueError:
            print('\033[33m' f'{ALICE_HOST_NAME} received message: '
                  f'{alice_server_address}\033[m')


if __name__ == "__main__":
    argc: int = len(argv)  # of command line arguments
    i: int = 1
    t: int = 2  # Default timeout set here
    q: str = ''

    while i != argc:
        if argv[i] == '-t' or argv[i] == '--timeout':
            try:
                _t = int(argv[2])
                if _t <= 0:
                    push_warn(f'Warning: timeout fallback to default {t}')
                t = _t
                i += 1
            except IndexError:
                push_error('No timeout set')
                exit(1)
            except ValueError:
                push_error(f'Invalid -t argument {argv[i + 1]}')
                exit(1)
        else:
            q = argv[i]

        i += 1

    try:
        main(query=q, time_limit=t)
    except KeyboardInterrupt:
        print('\033[31m' 'Process interrupted by user.' '\033[m')

CLIENT_SOCKET.close()
