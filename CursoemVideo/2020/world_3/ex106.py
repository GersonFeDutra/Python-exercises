def py_help() -> None:
    line_size: int = 30
    line: str = "-" * line_size

    print(f'\033[30;46m{line}\n{"Welcome to PyHelp!".center(line_size)}\n{line}')

    while True:
        entry: str = input('\033[mFunction or library: ')

        if entry == 'close':
            print(f'\033[07;31;47m{line}\n{"Closing PyHelp!".center(line_size)}\n{line}')
            print('\033[m')
            break

        print(f'\033[07;38;47m{line}\n{f"Accessing the token {entry}".center(line_size)}\n{line}')
        print('\033[m''\033[07;38;47m')
        help(entry)
        print('\033[m')


py_help()
