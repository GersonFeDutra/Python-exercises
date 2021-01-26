numbers: list = [int(input('Enter an integer: '))]


def ask() -> bool:
    return input('Do you want to continue? (y/n) ').lower() == 'y'


while ask():
    numbers.append(int(input('Enter an integer: ')))

print(f'''
The medium between all entered numbers is {sum(numbers) / len(numbers):.2f}.
The bigger number is: {max(numbers)}.
The smaller number is: {min(numbers)}.''')
