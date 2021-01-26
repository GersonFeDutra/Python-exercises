from random import choice

NUMBER_OF_CLASSMATES: int = 4
classmates: list = []

print(
    'The teacher wants a classmate to erase the blackboard.\n'
    f'Enter the name of {NUMBER_OF_CLASSMATES} of the classmates.'
)

for i in range(0, NUMBER_OF_CLASSMATES):
    classmates.append(input(f'{i + 1}: '))

print(f'\nThe chosen classmate is: {choice(classmates)}')
