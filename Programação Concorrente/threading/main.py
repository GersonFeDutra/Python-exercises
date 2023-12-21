"""Multi-threading."""
from threading import Thread
# import threading
import time


DONE = False


def worker(text: str) -> None:
    """Worker thread."""
    # global DONE
    counter: int = 0

    while not DONE:
        time.sleep(1)
        counter += 1
        print(f'{text}: {counter}')


def main() -> None:
    """Start point."""
    # Starts worker in a separate thread.
    threads: list[Thread] = []
    threads[0] = Thread(target=worker, daemon=True, args=("Counter 1",))
    threads[1] = Thread(target=worker, daemon=True, args=("Counter B",))
    # Daemon makes the thread quit at end of execution of non-daemon threads

    for thread in threads:
        thread.start()

    # for thread in threads:
    #     thread.join()

    while not DONE:
        input("Press enter to quit")


if __name__ == "__main__":
    main()
