values: list = [[], []]

for i in range(1, 8):
    value: float = float(input(f'Enter the {i}° number: '))

    if value % 2 == 0:
        values[0].append(value)
    else:
        values[1].append(value)

values[0].sort()
values[1].sort()
print('The even numbers are:', values[0])
print('The odd numbers are:', values[1])
