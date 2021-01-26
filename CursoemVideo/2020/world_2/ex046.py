from time import sleep
from emoji import emojize

for i in range(10, -1, -1):
    print(f'\033[{29 + i}m{i}\033[m')
    sleep(1)

print(emojize('\033[31m:fireworks: CA-BOOM!!!\033[m'))
