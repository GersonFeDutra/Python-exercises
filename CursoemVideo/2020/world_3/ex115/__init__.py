from file import *
from menu import *

file_name: str = "entries.txt"

if not file_exists(file_name):
    create_file(file_name)

while True:
    choice = show_menu(['See entries.', 'Add new entry.', 'Exit.'])

    if choice == 1:
        print(f'{"-" * 30}\n{"Name":26} {"Age"}')

        for line in read_file(file_name):
            data: list = line.split(';')
            data[1] = data[1].replace("\n", "")
            print(f'{data[0]:26} {data[1]:>3}')

    elif choice == 2:
        append_to_file(file_name, f'{input("Enter a name: ")};{input_int("Enter a age: ")}')
    else:
        break
