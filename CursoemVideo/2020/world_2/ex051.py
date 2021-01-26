print('=' * 40 + f'\n{"Arithmetic progression: 10 terms." :^40}\n' + '=' * 40)

first: int = int(input('Enter the first term: '))
reason: int = int(input('Enter the reason: '))

# PA:
# first_term: float
# number_of_terms: int
# reason: float
# last_term: float = first_term + (number_of_terms - 1) * reason # General term
#
# Extended formulae:
# n: int # position of term in the PA
# m: int
# m_term: float
# n_term: float = m_term + (n - m) * reason
#
# PA Sum:
# sum_of_terms: float = (first_term + last_term) * number_of_terms / 2

for i in range(0, 10):
    print(first, end=' → ')
    first += reason

# Alternative solution
# tenth_term: int = first + (10 - 1) * reason
#
# for i in range(first, tenth_term, reason):
#     print(f'{i}', end=' → ')

print('...')
