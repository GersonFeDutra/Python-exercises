NUMBER_OF_PEOPLE: int = 4

women_with_less_than_21_years: int = 0

people_names: list = []
people_ages: list = []
people_genders: list = []

for i in range(0, NUMBER_OF_PEOPLE):

    print(f'{f"{i + 1}° person" :_^20}')
    people_names.append(input('Name: '))
    people_ages.append(int(input('Age: ')))
    people_genders.append(input('Gender: (m / f) ').lower())

    if people_genders[i] == 'f' and people_ages[i] < 20:
        women_with_less_than_21_years += 1

print(f'''The medium of ages in this group is {sum(people_ages) // NUMBER_OF_PEOPLE}.
The older man is {people_names[people_ages[people_ages.index(max(people_ages))]]}.
The number of women with less than 21 years is {women_with_less_than_21_years}.''')
