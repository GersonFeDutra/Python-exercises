start: int = int(input('Enter integers iterations steps.\nStart at: '))
end: int = int(input('End at: '))
step: int = int(input('Step: '))

for i in range(start, end + 1 if end > start else end - 1, step):
    print(i)
