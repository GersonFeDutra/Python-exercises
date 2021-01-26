# from math import factorial

number: int = int(input('Enter an integer: '))
factorial: int = max(1, number)

print(f'{number}!', end=' ')

if factorial != 1:
    print(f'= {number}', end=' ')

while number > 1:

    number -= 1
    factorial *= number
    print(f'x {number}', end=' ')

print(f'= {factorial}.')

# Faster solution.
# print(f'The factorial of {number} is {factorial(number)}.')
