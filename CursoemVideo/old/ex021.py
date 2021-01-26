from pygame import init, mixer, event
init()
mixer.music.load('ex021.wav')
mixer.music.play()
event.wait()
