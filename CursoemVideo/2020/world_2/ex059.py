option: int = -1
values: list


def get_values() -> list:

    return [
        float(input('Enter a number: ')),
        float(input('Enter another number: '))
    ]


values = get_values()

while option != 5:

    option = int(input('\n[1] Sum\n[2] Multiply\n[3] Bigger\n[4] New numbers\n[5] Exit\n\033[32m>>> \033[m'))

    if option == 1:
        print(f'{values[0]} + {values[1]} = {values[0] + values[1]}.')

    elif option == 2:
        print(f'{values[0]} x {values[1]} = {values[0] * values[1]}.')

    elif option == 3:
        print(f'{values[0]} {">" if values[0] > values[1] else "<"} {values[1]}')

    elif option == 4:
        values = get_values()
