numbers: list = [int(input('[I will sum all numbers you type in. Press 999 to finish.]\nEnter an integer: '))]

while numbers[-1] != 999:
    numbers.append(int(input('Enter another integer: ')))

print(f'The sum of all {len(numbers) -1} entered numbers was {sum(numbers[:-1])}.')
