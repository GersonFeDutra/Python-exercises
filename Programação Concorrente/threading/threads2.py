"""Threads study."""
from threading import Thread, current_thread
from random import randint
from time import sleep


def task(_min: int, _max: int) -> None:
    """Do task."""
    sleep(randint(0, 10))
    print(current_thread().name)
    print(randint(_min, _max))


def main() -> None:
    """Execute starts."""
    threads: list[Thread] = []

    threads[0] = Thread(target=task, args=(0, 10,), name='Tarefa 01')
    threads[1] = Thread(target=task, args=(10, 100,), name='Tarefa 02')
    threads[2] = Thread(target=task, args=(100, 1000,), name='Tarefa 03')
    threads[4] = Thread(target=task, args=(1000, 10000,), name='Tarefa 04')

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
