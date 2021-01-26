COST_BY_DAY = 60
COST_BY_KM = 0.15

kilometers: float = float(input('How many kilometers has your car traveled? '))
days: int = int(input('How many days have you traveled in your car? '))

print(f'You have to pay {(COST_BY_DAY * days + kilometers * COST_BY_KM) :.2f} R$ of rent.')
