def file_exists(file_name: str) -> bool:
    exists: bool

    try:
        file = open(file_name, 'rt')
        file.close()
    except FileNotFoundError:
        exists = False
    else:
        exists = True

    return exists


def create_file(file_name: str) -> None:
    try:
        file = open(file_name, 'wt+')
        file.close()
    except Exception as error:
        print(f'\033[31mError creating file: {error}\033[m')


def read_file(file_name: str) -> list:
    contents: list = []

    try:
        file = open(file_name, "rt")

    except Exception as error:
        print(f'\033[31mError reading file "{file_name}": {error}\033[m')
    else:
        contents = file.readlines()
        file.close()

    return contents


def append_to_file(file_name: str, content: str) -> None:
    try:
        file = open(file_name, "at")
    except Exception as error:
        print(f'\033[31mError reading file "{file_name}": {error}\033[m')
    else:
        try:
            file.write(f'{content}\n')
        except Exception as error:
            print(f'\033[31mError writing at file "{file_name}": {error}\033[m')

        file.close()
