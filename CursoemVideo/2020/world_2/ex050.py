s: int = 0
number: int

for i in range(1, 7):
    number = int(input(f'Enter the {i}° integer: '))

    if number % 2 == 0:
        s += number

print('The sum of the odd numbers is:', s)
