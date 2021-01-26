from time import sleep


def counter(start: int, end: int, step: int) -> None:
    count: int = start
    step = abs(step)
    sleep(.5)

    if step == 0:
        step = 1

    if start < end:
        while count <= end:
            print(count, end='')
            count += step
            print(end=(', ' if count <= end else '.'), flush=True)
            sleep(.25)
    else:
        while count >= end:
            print(count, end='')
            count -= step
            print(end=(', ' if count >= end else '.'), flush=True)
            sleep(.25)
    print()


counter(1, 10, 1)
counter(10, 0, 2)
counter(int(input('\nYou can define a count below_\nStart: ')), int(input('End: ')), int(input('Step: ')))
