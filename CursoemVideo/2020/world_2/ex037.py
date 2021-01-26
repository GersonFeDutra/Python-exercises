number: int = int(input('Enter an integer: '))
option: int = int(input('Choose a conversion base: \n1 - binary\n2 - octal\n3 - hexadecimal\n'))

if option == 1:
    print(f'The number is {number:b} in binary.')

elif option == 2:
    print(f'The number is {number:o} in octal.')

elif option == 3:
    print(f'The number is {number:x} in hexadecimal.')

else:
    print('\033[31m''Invalid option, try again.\033[m')
