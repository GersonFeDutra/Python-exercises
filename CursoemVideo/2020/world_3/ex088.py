from random import randint
from time import sleep

plays: list = []
print('MEGA SENA')

for play in range(int(input('How many games do you want to generate? '))):
    sorted_values: list = []

    for i in range(6):
        sorted_value: int = randint(1, 60)

        while sorted_value in sorted_values:
            sorted_value = randint(1, 60)

        sorted_values.append(sorted_value)

    plays.append(sorted_values)

print('\nAll sorted games are:')

for i, play in enumerate(plays):
    sleep(1)
    print(f'{i + 1}° play: {play}')

sleep(1)
print('\nGood luck!')
