pupils: list = []


def want_continue() -> bool:
    answer: str = ''

    while answer not in ('y', 'n'):
        answer = input('Do you want to continue? (y/n) ').lower()

    return answer == 'y'


def arithmetic_medium(numbers: list) -> float:
    return sum(numbers) / len(numbers)


print('Enter the name and notes from each pupil from your class_')

while True:
    pupils.append([input('Name: '), []])

    for i in range(1, 3):
        pupils[-1][1].append(float(input(f'{i}th note: ')))

    if not want_continue():
        break

print(f'\n{"N°":4} {"NAME":20} {"MEDIUM":>6}')

for i, pupil in enumerate(pupils):
    print(f'{i:<4} {pupil[0]:20} {arithmetic_medium(pupil[1]):>6.2f}')

while True:
    entry: int = int(input('\nDo you want to see the notes from which pupil? (Enter -1 to stop): '))

    if entry == -1:
        break
    else:
        print(f'{pupils[entry][0]} notes are:', end=' [')

        for i, note in enumerate(pupils[entry][1]):
            print(note, end=('' if i == len(pupils[entry][1]) - 1 else ', '))

        print(']')
