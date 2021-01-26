from random import randint
from pygame import mixer
from time import sleep

jokenpo: list = ['\033[32m''Rock\033[m', '\033[34m''Paper\033[m', '\033[31m''Scissor\033[m'] # Também pode ser escrito entre parênteses: ('Rock', 'Paper', 'Scissor')
randomized: int = randint(0, 2)
option: int = int(input('''\
Let\'s play Jokenpô
\033[32m1 - Rock\033[m
\033[34m2 - Paper\033[m
\033[31m3 - Scissor\033[m
''')) - 1

for song in ['JO', 'KEN', 'PO!!!']:
    print(song)
    sleep(1)

print(f'You chose {jokenpo[option]} and I chose {jokenpo[randomized]}', end=' ')

if randomized == option:
    print('we have a\033[33m draw!\033[m')

elif (randomized == 0 and option == 1) or (randomized == 1 and option == 2) or (randomized == 2 and option == 1):
    mixer.init()
    print('\033[30myou Win!\033[m')
    mixer.music.load('final-fantasy-vii-victory-fanfare-1.mp3')
    mixer.music.play()
    sleep(4)

else:
    print('\033[37m''you lost!\033[m')
