height: float = float(input('What is the height of your wall? (meters) '))
width: float = float(input('What is the width of your wall? (meters) '))
area = height * width

print(f'The wall area is {area}m². To paint it you will need {area / 2 :.3f}l of ink.')
