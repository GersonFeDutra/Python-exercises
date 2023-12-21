#!/usr/bin/python3
'''
Ping Client
'''
from time import time
from sys import argv, stderr
from socket import AF_INET, SOCK_DGRAM, socket, timeout

HOST: str = '127.0.0.1'  # Connect to localhost
PORT: int = 50000  # Server port
SERVER_ADDRESS = (HOST, PORT)  # Server configuration
DATA_PAYLOAD: int = 1024  # The maximum amount of data to be received at once


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


def main(show_ttl: bool = False, time_limit: int = 0,
         pings_n=10, *_args) -> None:
    '''
    @param:
        time_limit: time to timeout, 0 or negative fallback to default
        pings_n: #of pings requested to the server
    '''
    if time_limit <= 0:
        time_limit = 2

    lost_packets_n: int = 0
    rtt_list: list[float] = []  # Saves Road-Trip Time for each message

    # Create a UDP socket
    client_socket = socket(AF_INET, SOCK_DGRAM)

    # Set time limit (sec)
    client_socket.settimeout(time_limit)

    # Send pings to the server (default to 10)
    for i in range(pings_n):
        message = f'Ping {i + 1}'.encode()
        start_time = time()  # (s) Used to account the ping shipping time

        print(f'Request: {message}')
        client_socket.sendto(message, SERVER_ADDRESS)

        try:
            response, server = client_socket.recvfrom(DATA_PAYLOAD)

            if show_ttl:
                # Road-Trip Time (converted to ms)
                rtt = (time() - start_time) * 1000
                rtt_list.append(rtt)

                print(f"Response from {server}: {response.decode()}")
                print(f"Round-trip time: {rtt:.3f} ms\n")
            else:
                # Time taken for the message
                end_time: float = time() - start_time
                print(f'Received "{response.decode()}" '
                      f'from {server} in {end_time * 1000:.3f}ms')

        except timeout:
            lost_packets_n += 1
            push_warn('Ping request timed out')

    client_socket.close()

    if show_ttl:
        # Calculate RTT list statistics
        packet_loss_rate: float = lost_packets_n / pings_n
        if len(rtt_list) > 0:
            min_rtt: float = min(rtt_list)
            max_rtt: float = max(rtt_list)
            avr_rtt: float = sum(rtt_list) / len(rtt_list)
        else:
            min_rtt, max_rtt, avr_rtt = 0, 0, 0

        print('Road-Tript Time statistics:')
        print(f'\tMinimum RTT: {min_rtt:.3f} ms')
        print(f'\tMaximum RTT: {max_rtt:.3f} ms')
        print(f'\tAverage RTT: {avr_rtt:.3f} ms')
        print(f'\nPacket loss rate: {packet_loss_rate * 100:.2f}%')


if __name__ == "__main__":
    argc: int = len(argv)  # of command line arguments
    i: int = 1
    t: int = 2  # Default timeout set here
    a: bool = False
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
        elif argv[i] == '-a' or argv[i] == '--advanced':
            a = True
        else:
            push_warn('Invalid option')

        i += 1

    try:
        main(show_ttl=a, time_limit=t)
    except KeyboardInterrupt:
        print('\033[31m' 'Process interrupted by the user.' '\033[m')
