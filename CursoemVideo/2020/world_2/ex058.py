# ex028 UPDATED
from time import sleep
from random import randint

tries: int = 1
randomized: int = randint(0, 10)
choice: int = -1


def won_the_game() -> bool:
    global randomized, choice
    win: bool

    print('Make your guess:', end=' ')

    if 5 >= choice >= 0:
        print(('(more) ' if choice < randomized else '(less) '), end='')

    choice = int(input())
    win = randomized == choice
    print('PROCESSING...')
    sleep(1.5)
    print(f'\033[{"32m""You win" if win else "31m""Wrong"}!\033[m\n')

    return win


print(('-=' * 41) + f'-\n{"I will think a number between 0 and 10. Can you guess which number it is?":^82}\n' + ('-=' * 41) + '-')

while not won_the_game():  # Equivalent to `do while`
    tries += 1
    print('\033[35mTry Again:\033[m')

print(f'You won with {tries} tries.')
