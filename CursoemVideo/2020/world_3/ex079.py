numbers: list = []


def want_continue() -> bool:
    answer: str = ''

    while answer not in ('y', 'n'):
        answer = input('Do you want to continue? (y/n) ').lower()

    return answer == 'y'


while True:
    number: float = float(input('Enter a number: '))

    if number not in numbers:
        numbers.append(number)
        print('Value added successfully!')

    else:
        print('Value duplicated, will not be added.')

    if not want_continue():
        break

numbers.sort()
print('\nAll the entered values are:', numbers)
