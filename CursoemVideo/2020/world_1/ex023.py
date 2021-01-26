# Math solution
# number: int = int(input('Enter a number between 0 and 9999: '))
#
# print(f"""
# Unity: {number % 10}
# Dozen: {(number // 10) % 10}
# Hundred: {(number // 100) % 10}
# Thousand: {(number // 1000) % 10}""") # Nesse caso o "% 10" é ultilizado como caso o usuário digite um valor maior que 9999. Mas não é estritamente necessário.

# Strings solution # Boring way
# number: str = input('Enter a number between 0 and 9999: ')
#
# print(f"""
# Unity: {number[-1] if len(number) > 0 else '0'}
# Dozen: {number[-2] if len(number) > 1 else '0'}
# Hundred: {number[-3] if len(number) > 2 else '0'}
# Thousand: {number[-4] if len(number) > 3 else '0'}""")

# Strings solution # Nice way
# number: str = str(int(input('Enter a number between 0 and 9999: ')) + 10000)  # Geitinho Brazileiro :V
number: str = input('Enter a number between 0 and 9999: ').zfill(4)  # Brazilian Little Way Remix :D

print(f"""
Unity: {number[-1]}
Dozen: {number[-2]}
Hundred: {number[-3]}
Thousand: {number[-4]}""")
