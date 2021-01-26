# ex035 UPDATED
print('Enter 3 lengths (cm): ')
lengths: list = []


def get_triangle_type() -> str:
    global lengths
    value: str

    if lengths[0] == lengths[1] == lengths[2]:
        value = '\033[33m''equilateral\033[m'

    elif lengths[0] != lengths[1] != lengths[2] != lengths[0]:
        value = '\033[33m''scalene\033[m'

    else:
        value = '\033[33m''isosceles\033[m'

    return value


# Using operations
# def get_triangle_type() -> str:
#     global lengths
#     value: str
#     equals: int = int(lengths[0] == lengths[1]) + int(lengths[1] == lengths[2]) + int(lengths[2] == lengths[0])
#
#     if equals == 0:
#         value = '\033[33m''scalene\033[m'
#
#     elif equals == 1:
#         value = '\033[33m''isosceles\033[m'
#
#     else:
#         value = '\033[33m''equilateral\033[m'
#
#     return value


for i in range(3):
    lengths.append(float(input(f'{i + 1}°: ')))

if lengths[0] < lengths[1] + lengths[2] and lengths[1] < lengths[0] + lengths[2] and lengths[2] < lengths[0] + lengths[1]:
    print(
        'You\033[32m can\033[m form a triangle with this lengths.'
        f'\nThe triangle is {get_triangle_type()}.'
    )

else:
    print('You\033[31m cannot\033[m form a triangle with this lengths.')
