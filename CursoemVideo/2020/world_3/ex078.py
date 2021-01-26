largest: int = int(input('Enter an integer to position 0: '))
largest_positions: list = [0]
lowest: int = largest
lowest_positions: list = largest_positions[:]

for i in range(1, 5):
    num: int = int(input(f'Enter an integer to position {i}: '))

    if num == largest:
        largest_positions.append(i)

    elif num > largest:
        largest = num
        largest_positions = [i]

    if num == lowest:
        lowest_positions.append(i)

    elif num < lowest:
        lowest = num
        lowest_positions = [i]

print(f'The largest entered number is {largest}, it was entered in the positions:{largest_positions}.')
print(f'The lowest entered number is {lowest}, it was entered in the positions:{lowest_positions}.')
