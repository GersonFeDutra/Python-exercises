people: list = []
data: list = []

for i in range(0, 3):
    data.append(input('Name: '))
    data.append(int(input('Age: ')))
    people.append(data[:])
    #people.append(data) # Sem fatiamento, o array será passado como referência, ao invés de por cópia.
    data.clear() # Logo a lista adicionada à 'people' também seria esvaziada.

print(people) # Terá como saída, uma lista contendo sub-listas com os dados entrados pelo usuário.

total_major: int = 0
total_minor: int = 0

for person in people:
    if person[1] > 20:
        print(person[0], 'is major.')
        total_major += 1
    else:
        print(person[0], 'is under age.')
        total_minor += 1

print(f'We have {total_major} major people, and {total_minor} under age people')
