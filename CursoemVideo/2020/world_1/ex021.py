# from playsound import playsound
#
# print('Let\'s play a sound :) ')
# playsound('../ex021.wav')
# # playsound('hello_world.mp3') # Doesn't work for some reason.

# Usando o PyGame
from pygame import mixer
import time

print('Let\'s play a sound :) ')
mixer.init()
mixer.music.load('../hello_world.mp3')
mixer.music.play()
time.sleep(1 * 60 + 53)
