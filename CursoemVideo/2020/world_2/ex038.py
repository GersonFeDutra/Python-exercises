numbers: list = [
    int(input('Enter an integer: ')),
    int(input('Enter another integer: '))
]

if numbers[0] > numbers[1]:
    print(f'The number {numbers[0]} is bigger than the number {numbers[1]}')

elif numbers[0] < numbers[1]:
    print(f'The number {numbers[0]} is smaller than the number {numbers[1]}')

else:
    print('The two entered numbers are equal.')
