imc: float = float(input('What is your weight? (kg) ')) / float(input('What is your height? (m) ')) ** 2


def get_status() -> str:
    global imc
    status: str

    if imc < 18.5:
        status = '\033[35m''under weight\033[m'

    elif imc < 25:
        status = '\033[32m''ideal weight\033[m'

    elif imc < 30:
        status = '\033[34m''overweight\033[m'

    elif imc < 40:
        status = '\033[33m''obese\033[m'

    else:
        status = '\033[31m''morbidly obese\033[m'

    return status


print(f'Your IMC is {imc:.1f}. You are {get_status()}.')
