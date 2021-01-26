distance: int = int(input('Enter a travel distance (km): '))
print(f'The ticket\'s price is R${distance * (0.5 if distance <= 200 else 0.45) :.2f}.')
