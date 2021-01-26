numbers: list = []

for i in range(0, 5):
    num: float = float(input('Enter a number: '))
    position: int = 0

    for number in numbers:
        if number < num:
            position += 1
        else:
            break

    numbers.insert(position, num)

    if position == 0:
        print('Added to the start of the list.')

    elif position == len(numbers) - 1:
        print('Added to the end of the list.')

    else:
        print(f'Added in the position {position} of the list.')

print('The entered values in order are:', numbers)
