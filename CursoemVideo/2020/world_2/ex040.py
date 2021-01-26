SEMESTERS: int = 2
medium: float
notes: list = []

for i in range(SEMESTERS):
    notes.append(float(input(f'What is your {i + 1}° note? ')))

medium = sum(notes) / SEMESTERS
print(f'Your medium is {medium:.1f}.')

if medium < 5:
    print('\033[31mDISAPPROVED!')

elif medium < 7:
    print('\033[33mRECOVERY!')

else:
    print('\033[32mAPPROVED!')
