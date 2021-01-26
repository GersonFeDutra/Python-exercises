from time import sleep
from random import randint

random: int = randint(0, 5)
number: int

print(('-=' * 41) + '-\nI will think a number between 0 and 5. Can you guess which number it is?\n' + ('-=' * 41) + '-')
number = int(input('Make your guess: '))
print('PROCESSING...')
sleep(1.5)
print(f'The number that I guessed was {random}. You {"win" if random == number else "lose"}!')
