people: list = []
women: list = []
medium_age: float = 0
entries_entered: int


def get_from_options(options: tuple, message: str) -> str:
    option: str = ''

    while option not in options:
        option = input(message).lower()

    return option


print('Enter the people data: ')

while True:
    person: dict = {
        'name': input('Name: '),
        'gender': get_from_options(('m', 'f', 'o'), 'Gender: (m, f, o) '),
        'age': int(input('Age: '))
    }
    medium_age += person['age']
    people.append(person)

    if person['gender'] == 'f':
        women.append(person)

    if get_from_options(('y', 'n'), 'Do you want to continue? ') == 'n':
        break

entries_entered = len(people)
medium_age /= entries_entered
print(f'\n{entries_entered} people were entered.')
print(f'The medium age from the group of people is {medium_age:.1f}')
print('All the women: [')

for woman in women:
    print("    ", woman)

print(']')
print('All the people over the medium age: [')

for person in people:
    if person['age'] > medium_age:
        print("    ", person)

print(']')
