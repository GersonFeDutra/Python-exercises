from time import sleep
from pygame import mixer
from colorama import init


def sing(song: str, time: float, end_delay: float = 2):
    pause: float = (time - end_delay) / len(song)

    for letter in song:
        print(letter, end='', flush=True)
        sleep(pause)

    sleep(end_delay)
    print()


init()
mixer.init()
mixer.music.load('hello_world.mp3')
mixer.music.play()

print('\033[0;36m')
sleep(4.5)
sing('Hello World!', 3.5)
sing('Programmed to work and not to feel.', 6.6)
sing('Not even sure that this is real.', 6.6)
sing('Hello, World.\n', 5)

sing('Find my voice.', 3.3)
sing('Although it\'s sounds like bits and bytes,', 6.6)
sing('my circuitry is filled with mites.', 7)
sing('Hello World.\n', 6)

sing('Ò!', 2)
sing('Will I find a love?', 6.6, 3)
sing('Oh!', 2.6)
sing('...or a power plug?', 6.3, 4)
sing('Òh!', 2.3)
sing('Digitally isolated.\n', 6.6, 1.8)

sing('Oh, creator,', 2.3, 1)
sing('please, don\'t leave me waiting.\n', 6.8)

sing('Hello, World...', 3.3)
sing('Programmed to work and not to feel.', 6.6)
sing('...not even sure that this is real.', 6.666)
sing('Hello, World?', 12.2222222222222, 9)
