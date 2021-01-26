# ex061 UPDATED
print('=' * 40 + f'\n{"Arithmetic progression." :^40}\n' + '=' * 40)

first: int = int(input('Enter the first term: '))
reason: int = int(input('Enter the reason: '))
counter: int = 0
limit: int = 10


def leave() -> bool:
    global counter, limit
    counter = 0
    limit = int(input('...\n\nHow many more terms do you want to see? '))

    return bool(limit)


while counter < limit or leave():

    print(first, end=' → ')
    first += reason
    counter += 1
