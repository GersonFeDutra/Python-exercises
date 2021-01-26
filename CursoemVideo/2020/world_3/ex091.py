from random import randint
from time import sleep
from operator import itemgetter

# Using built-in sorted() with method itemgetter()
cache: dict = {}
results: list

for i, person in enumerate(('João', 'Pedro', 'Lucas', 'Maria')):
    cache[person] = randint(1, 6)

    print(f'The {i + 1}th player {person} got {cache[person]}.')
    sleep(1)

results = sorted(cache.items(), key=itemgetter(1), reverse=True)

for i, entry in enumerate(results):
    print(f'{i + 1}th Place: {entry[0]} with {entry[1]}')

# Hard Coded Solution
# cache: list = []
# results: dict = {}
#
# for i, person in enumerate(('João', 'Pedro', 'Lucas', 'Maria')):
#     results[person] = randint(1, 7)
#
#     print(f'The {i + 1}th player {person} got {results[person]}.')
#     sleep(1)
#
# for person, result in results.items():
#     counter: int = 0
#
#     for entry in cache:
#
#         if result > list(entry.values())[0]:
#             counter += 1
#
#     cache.insert(counter, {person: result})
#
# cache.reverse()
# results = {}
# print('\nRanking_')
#
# for i, entry in enumerate(cache):
#     person: str = list(entry.keys())[0]
#     result: int = list(entry.values())[0]
#     results[person] = result
#     print(f'{i + 1}th Place: {person} with {result}')
