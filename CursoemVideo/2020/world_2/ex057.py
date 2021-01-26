gender: str = input('What is your gender? (M/F) ').upper()

while gender != 'M' and gender != 'F':

    gender = input(
        '\n\033[31mYou must enter only M or F. Please, try Again:\033[m'
        '\nWhat is your gender? (M/F) '
    ).upper()
