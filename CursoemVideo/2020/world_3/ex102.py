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


print(factorial(5))
print(' =', factorial(5, True))
result: int = factorial(10, True)
print()
print(f'{result:>38}')
help(factorial)
