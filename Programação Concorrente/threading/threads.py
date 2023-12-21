"""Threading study."""
from threading import Thread, current_thread
from random import randint
from time import sleep


def work(_min: int, _max: int) -> None:
    """Working thread."""
    sleep(randint(1, 4))
    print(current_thread().name)
    print(randint(_min, _max))


thread1 = Thread(target=work, args=(1, 2,), name='Nome')
