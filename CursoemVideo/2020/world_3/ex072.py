numbers: tuple = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                  'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
number: int = int(input('Enter an integer between 0-20: '))


def want_continue() -> bool:
    answer: str = ''

    while answer not in ('n', 'y'):
        answer = input('Do you want to continue? (y/n) ').lower()

    return answer == 'y'


while not(0 <= number <= 20 and not want_continue()):
    number = int(input('Try again. Enter an integer between 0-20: '))

print(f'{number} in full is {numbers[number]}.')
