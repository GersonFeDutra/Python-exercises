numbers: tuple = (int(input('Enter an integer: ')), int(input('Enter another integer: ')),
                  int(input('Enter another integer: ')), int(input('Enter another integer: ')),
                  int(input('Enter another integer: ')))
even_numbers: list = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(f'The number 9 have appeared {numbers.count(9)} times.')

if 3 in numbers:
    print(f'The first value 3 was entered at the {numbers.index(3) + 1}th entry.')
else:
    print('The value 3 was never entered.')

if len(even_numbers) > 0:
    print(f'The even numbers are {even_numbers}.')
else:
    print('There are no even numbers.')
