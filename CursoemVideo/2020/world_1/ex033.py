AMOUNT: int = 3
numbers: list = []

for i in range(AMOUNT):
    numbers.append(int(input(f'{i + 1}°: ')))

# Smarter way
numbers.sort()
print(f'The bigger number is {numbers[AMOUNT - 1]}, and the smaller number is {numbers[0]}')

# Setting orders manually
# bigger: int
# smaller: int
# 
# 
# def set_extremes(number: int):
#     """
#     Define the extremes values: bigger and smaller
#     :param number: The value to be checked.
#     """
#     global bigger, smaller
# 
#     if number > bigger:
#         bigger = number
# 
#     if number < smaller:
#         smaller = number
# 
# 
# print('Enter 3 numbers: ')
# numbers.append(int(input('1°: ')))
# bigger = numbers[0]
# smaller = numbers[0]
# 
# for i in range(1, 3):
#     numbers.append(int(input(f'{i + 1}°: ')))
#     set_extremes(numbers[i])
# 
# print(f'The bigger number is {bigger}, and the smaller number is {smaller}')
