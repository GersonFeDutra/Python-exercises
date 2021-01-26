from random import shuffle

NUMBER_OF_CLASSMATES: int = 4
classmates: list = []

print(
    'The teacher wants to sort the presentation order of each classmate to show their classwork.'
    f'\nEnter the name of {NUMBER_OF_CLASSMATES} of the classmates.'
)

for i in range(0, NUMBER_OF_CLASSMATES):
    classmates.append(input(f'{i + 1}: '))

shuffle(classmates)
print(f'\nThe presentation order of classmates is, respectively:')

for i in range(0, NUMBER_OF_CLASSMATES):
    print(f'{i + 1}°: {classmates[i]}')
