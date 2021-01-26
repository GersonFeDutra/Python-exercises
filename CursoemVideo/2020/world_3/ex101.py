def vote(birth: int) -> str:
    from datetime import date

    years: int = date.today().year - birth
    message: str = f'With {years} your vote is '

    if years < 16:
        message += 'DENIED'
    elif years <= 18 or years >= 65:
        message += 'OPTIONAL'
    else:
        message += 'MANDATORY'

    return message


print(vote(int(input('What year were you born? '))))
