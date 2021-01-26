matrix: list = [[], [], []]

for i in range(3):
    for j in range(3):
        matrix[i].append(float(input(f'Enter a value to the position [{i}, {j}]: ')))

print()

for i in range(3):
    for j in range(3):
        print(f'|{matrix[i][j]:^7.1f}', end='')
    print('|')
