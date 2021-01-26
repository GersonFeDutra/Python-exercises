from random import randint


def bigger(*values) -> None:

    if len(values) > 0:
        print('Analysing the received values:', values)
        print('The biggest value is', max(values))
        print()
    else:
        print('No values were received!')


bigger(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10))
bigger(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10))
bigger(randint(-10, 10), randint(-10, 10), randint(-10, 10))
bigger(randint(-10, 10), randint(-10, 10))
bigger(randint(-10, 10))
bigger()
