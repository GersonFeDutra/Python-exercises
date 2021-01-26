numbers: list = []
even_numbers: list = []
odd_numbers: list = []


def want_continue() -> bool:
    answer: str = ''

    while answer not in ('y', 'n'):
        answer = input('Do you want to continue? (y/n) ').lower()

    return answer == 'y'


while True:
    num: float = float(input('Enter a number: '))
    numbers.append(num)

    if num % 2 == 0:
        even_numbers.append(num)

    else:
        odd_numbers.append(num)

    if not want_continue():
        break

print('All the entered numbers are:', numbers)
print('All the even numbers are:', even_numbers)
print('All the odd numbers are:', odd_numbers)
