print('Enter 3 lengths (cm): ')
lengths: list = []

for i in range(3):
    lengths.append(float(input(f'{i + 1}°: ')))

# Arithmetic full right solution
# if abs(lengths[1] - lengths[2]) < lengths[0] < lengths[1] + lengths[2] \
#         and abs(lengths[0] - lengths[2]) < lengths[1] < lengths[0] + lengths[2] \
#         and abs(lengths[0] - lengths[1]) < lengths[2] < lengths[0] + lengths[1]:

# Algorithmic enough right solution
if lengths[0] < lengths[1] + lengths[2] and lengths[1] < lengths[0] + lengths[2] and lengths[2] < lengths[0] + lengths[1]:
    print('You can form a triangle with this lengths.')
else:
    print('You cannot form a triangle with this lengths.')
