salary: float = float(input('What is the functionary salary? R$ '))

print(f'His salary now is: {salary + salary * (10 if salary > 1250 else 15) / 100 :.2f} R$.')
