from datetime import date  # Another method is using the module datetime -> # datetime.now().year

MILITARY_AGE: int = 18
born_year: int = int(input('What year were you born? '))
age: int = date.today().year - born_year

print(f'Those born in {born_year} have to enlist in {born_year + MILITARY_AGE}.')

if age < MILITARY_AGE:
    print('You will still enlist in the military in the future. Come back in', MILITARY_AGE - age, 'year(s).')

elif age > MILITARY_AGE:
    print('You have passed the time to enlist in the military. You are', age - MILITARY_AGE, 'year(s) later.')

else:
    print('It\' time to enlist in the military.')
