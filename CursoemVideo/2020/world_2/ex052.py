number: int = int(input('Enter an integer: '))
is_prime: bool = True

for i in range(2, number // 2):

    if number % i == 0:
        is_prime = False
        break

print(f'The number {number}', '\033[32mis' if is_prime else '\033[31mis not', 'prime.\033[m')
