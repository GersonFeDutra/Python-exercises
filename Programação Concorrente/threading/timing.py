"""Checks for thread running timing."""
from time import time


def main(*_args) -> None:
    """Start program."""


if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print(f'{end - start}s')
