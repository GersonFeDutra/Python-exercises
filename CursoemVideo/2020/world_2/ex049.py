# ex09 UPDATED?? :v
number: int = int(input('Enter an integer to see its multiplication table: '))
print('_' * 12)

for i in range(1, 11):
    print(f'{number} x {i :2} = {number * i}')
