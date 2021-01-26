print(f'{" SHOPPING GUANABARA ":=^40}')
normal_price: float = float(input('What is the normal price of the product? R$ '))
option: int = int(input(
    'What is the condition of payment?'
    '\n1 - In Cash (money/ check)\n2 - In Cash (credit card)\n3 - Credit Card 2x\n4 - Credit Card 3x +\n')
)


def get_conditioned_price() -> float:
    global option, normal_price
    price: float = normal_price
    plots: int = 2

    if option == 1:
        price -= normal_price * 10 / 100

    elif option == 2:
        price -= normal_price * 5 / 100

    elif option == 3:
        print(f'Your purchase will be parceled out in {plots}x of R${price / 2:.2f} with interest.')

    elif option == 4:
        plots = int(input('In how many plots do you wanna to pay? '))
        price += normal_price * 20 / 100
        print(f'Your purchase will be parceled out in {plots}x of R${price / plots:.2f} with interest.')

    else:
        print('\033[31m''Invalid payment option.\033[m')

    return price


print(f'You gonna pay a total of R${get_conditioned_price():.2f} for this product.')
