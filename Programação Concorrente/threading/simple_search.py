"""Simple search in an array with threads."""
from threading import Thread, current_thread
from random import sample
from time import time

SIZE = 30000000
MAX = 30000000
N = 123456


def search(n: int, arr: list) -> None:
    """Do search."""
    for m in arr:
        if n == m:
            print(f'{current_thread().name} found!')


def main(*_args) -> None:
    """Do start."""
    array = sample(range(0, SIZE), SIZE)

    # Serial search
    start = time()
    search(N, array)
    end = time()
    print(f'Serial search: {end - start}s')

    # Concurrent search
    _slice: int = int(len(array) / 4)
    threads: list[Thread] = []

    start = time()
    for i in enumerate(threads):
        threads.append(Thread(target=search, args=(
            N, array[_slice * i:_slice * (i + 1)],), name=f'Task{i + 1}'))
    end = time()
    print(f'Concurrent search: {end - start}s')


if __name__ == '__main__':
    main()
