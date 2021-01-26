from random import randint

numbers: list = []


def draft_draw() -> None:
    print('Sorting 5 values:', end=' ')

    for i in range(5):
        numbers.append(randint(0, 10))
        print(f'({numbers[-1]})', end=' ')

    print()


def sum_even() -> None:
    result: int = 0
    print('Adding the even values:', end=' ')

    for number in numbers:
        if number % 2 == 0:
            result += number
            print(f'({number})', end=' ')

    print('=', result)


draft_draw()
sum_even()
