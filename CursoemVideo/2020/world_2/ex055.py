# Manually analyzing.
# people_weight: list = [float(input(f'What is the weight of the 1° person? (kg) '))]  # values initialized first
# bigger: float = people_weight[0]
# shorter: float = people_weight[0]
#
# for i in range(1, 5):
#     people_weight.append(float(input(f'What is the weight of the {i + 1}° person? (kg) ')))
#
#     if people_weight[i] > bigger:
#         bigger = people_weight[i]
#
#     if people_weight[i] < shorter:
#         shorter = people_weight[i]

# Optimized
people_weight: list = []

for i in range(0, 5):
    people_weight.append(float(input(f'What is the weight of the {i + 1}° person? (kg) ')))

print(
    f'From the 5 people entered, the bigger weight was {max(people_weight)} kg'
    f' and the shorter weight was {min(people_weight)} kg.'
)
