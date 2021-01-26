def input_int(message: str) -> int:
    entry: int = 0

    while True:
        try:
            entry = int(input(message))
        except KeyboardInterrupt:
            print('\033[33mExecution broken.\033[m')
            break
        except (ValueError, TypeError):
            print(f'\033[31mError! Enter a valid integer.\033[m')
            continue
        else:
            break

    return entry


def input_float(message: str) -> float:
    entry: float = 0.0

    while True:
        try:
            entry = float(input(message))
        except KeyboardInterrupt:
            print('\033[33mExecution broken.\033[m')
            break
        except (ValueError, TypeError):
            print(f'\033[31mError! Enter a valid real number.\033[m')
        else:
            break

    return entry


print('You just entered the number', input_int('Enter an integer: '))
print('You just entered the number', input_float('Enter a real number: '))
