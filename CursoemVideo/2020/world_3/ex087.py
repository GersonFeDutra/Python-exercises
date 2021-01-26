matrix: list = [[], [], []]
even_numbers: list = []
third_column_sum: float = 0

for i in range(3):
    for j in range(3):
        matrix[i].append(float(input(f'Enter a value to the position [{i}, {j}]: ')))

        if matrix[i][j] % 2 == 0:
            even_numbers.append(matrix[i][j])

print('\033[30m')

for line_id, line in enumerate(matrix):
    print(f'\033[4{line_id}m', end='')

    for column_id, number in enumerate(line):
        print(f'|\033[3{column_id + 3}m{number:^7.1f}', end='\033[30m')

    print('|\033[m\033[30m')
    third_column_sum += line[2]

print('\033[m')
print(f'The sum of all even numbers {even_numbers} is {sum(even_numbers)}.')
print('The sum of all values in the \033[35m' f'third column\033[m is {third_column_sum}.')
print('The biggest value from the \033[30;41m''second line\033[m is:', max(matrix[1]))
