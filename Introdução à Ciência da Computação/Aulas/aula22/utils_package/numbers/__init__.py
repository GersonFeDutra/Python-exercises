# This is the __init__ script from this package named 'numbers'.


def factorial(number: int, show: bool = False) -> int:
    """
    Calculates the factorial of a number.
    :param number: The number that will be calculated.
    :param show: If the calculation will be displayed.
    :return: int factorial of the number.
    """
    counter: int = 1

    for i in range(number, 0, -1):
        counter *= i

        if show:
            print(i, end=' x ' if i > 1 else '')

    return counter


def doble(n):
    return n * 2


def triple(n):
    return n * 3
