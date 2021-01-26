numbers: list = []


def want_continue() -> bool:
    answer: str = ''

    while answer not in ('y', 'n'):
        answer = input('Do you want to continue? (y/n) ').lower()

    return answer == 'y'


while True:
    numbers.append(float(input('Enter a number: ')))

    if not want_continue():
        break

print(len(numbers), 'numbers were entered.')
numbers.sort(reverse=True)
print('These numbers in descending order are:', numbers)
print('The number 5', 'was entered in the list.' if 5 in numbers else 'was not entered in the list.')
