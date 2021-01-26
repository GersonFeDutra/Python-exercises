def input_int(message: str) -> int:
    entry: str = ''

    while not entry.isnumeric():
        entry = input(message)

    return int(entry)


print('You just entered the number', input_int('Enter a number: '))
