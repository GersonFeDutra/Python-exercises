people: list = []
heavier: list
lighter: list


def get_data() -> list:
    return [
        input("Name: "),
        float(input('Weight: '))
    ]


def want_continue() -> bool:
    answer: str = ''

    while answer not in ('y', 'n'):
        answer = input('Do you want to continue? (y/n) ').lower()

    return answer == 'y'


print("Enter the people data_")
people.append(get_data())
heavier = [people[0][1], [people[0][0]]]
lighter = heavier[:]

while True:
    if not want_continue():
        break

    data: list = get_data()
    people.append(data[:])

    if data[1] > heavier[0]:
        heavier = [data[1], [data[0]]]

    elif data[1] == heavier[0]:
        heavier[1].append(data[0])

    if data[1] < lighter[0]:
        lighter = [data[1], [data[0]]]

    elif data[1] == lighter[0]:
        lighter[1].append(data[0])

print(f'\n{len(people)} persons were entered.')
print(f'The heaviest weight was {heavier[0]:.1f}kg, from: {heavier[1]}.')
print(f'The lighter weight was {lighter[0]:.1f}kg, from: {lighter[1]}.')
