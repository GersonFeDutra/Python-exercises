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


def input_from_range(from_: int, to: int, message: str) -> int:
    choice: int = to + 1

    while choice not in range(from_, to):
        choice = input_int(message)

    return choice


def show_menu(options_descriptions: list, input_message: str = 'Your option: ', line_size: int = 30) -> int:
    line: str = "-" * line_size
    choice: str

    print(f'{line}\n{"MENU".center(30)}\n{line}')

    for i, description in enumerate(options_descriptions):
        print(f'\033[33m{i + 1}\033[33m - \033[34m{description}\033[m')

    return input_from_range(1, len(options_descriptions) + 1, input_message)
