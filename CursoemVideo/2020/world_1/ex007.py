average: float = (
    float(input('What was your first semester note on the school last year? ')) +
    float(input('What was your second semester note on the school last year? '))
) / 2

print("Your average was {:.1f}".format(average))
print(f'Your average was {"good!" if average >= 6 else "bad."}')
