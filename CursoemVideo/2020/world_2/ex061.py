# ex051 UPDATED
print('=' * 40 + f'\n{"Arithmetic progression: 10 terms." :^40}\n' + '=' * 40)

first: int = int(input('Enter the first term: '))
reason: int = int(input('Enter the reason: '))
tenth_term: int = first + (10 - 1) * reason

while first != tenth_term:
    print(first, end=' → ')
    first += reason

print('...')
