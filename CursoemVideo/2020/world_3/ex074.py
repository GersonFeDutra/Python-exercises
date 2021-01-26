from random import randint

numbers: tuple = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'''From the randomized numbers {numbers}:
The lowest value is {min(numbers)};
And the largest value is {max(numbers)}.''')
