LIMIT: int = 80
velocity: int = int(input('What is the velocity of the automobile right now? (km/h) '))

if velocity > LIMIT:
    print(
        f'The automobile is above the velocity limit of {LIMIT}km/h. Therefore, the driver will be fined.'
        f'\nThe fine you cost him {(velocity - LIMIT) * 7}R$.'
    )
else:
    print(f'The automobile is below the velocity limit of {LIMIT}km/h.')
