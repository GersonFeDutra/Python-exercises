from datetime import date

data: dict = {
    'name': input('Name: '),
    'birth': int(input('Birth: ')),
    'wc': int(input('Work Card: (0 to none) '))
}
data['age'] = date.today().year - data['birth']

if data['wc'] > 0:
    data['hiring'] = int(input('Year of hiring: '))
    data['salary'] = float(input('Salary: '))
    data['retire'] = data['hiring'] + 35
    data['retire_age'] = data['retire'] - data['birth']

print(data)
