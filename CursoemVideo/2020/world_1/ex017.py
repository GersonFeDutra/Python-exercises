from math import hypot

opposite_side: float = float(input('What is the length of the opposite side of the rectangle triangle? (cm) '))
adjacent_side: float = float(input('What is the length of the adjacent side of the rectangle triangle? (cm) '))

# Manually calculating
# print(f'The hypotenuse of the triangle is: {(opposite_side ** 2 + adjacent_side ** 2) ** (1/2):.2f}cm')

# Using math
print(f'The hypotenuse of the triangle is: {hypot(opposite_side, adjacent_side):.2f}cm')
