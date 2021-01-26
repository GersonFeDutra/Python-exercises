DOLLAR_PRICE: float = 3.27
money: float = float(input('How much many money do you have now? R$'))

print('You can buy US${:.2f}.'.format(money / DOLLAR_PRICE))
