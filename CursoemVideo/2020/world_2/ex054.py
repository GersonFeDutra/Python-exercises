people_birth: list = []
majority: int = 0

for i in range(0, 7):
    people_birth.append(int(input(f'What year was the {i + 1}° person born? ')))

    if people_birth[i] >= 21:
        majority += 1

print(f'From the 8 people entered, {majority} get in the major age.')
