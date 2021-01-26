import coin

price = float(input('Enter a price: R$'))
print(f'Half: R${coin.half(price):.2f}')
print(f'Double: R${coin.double(price):.2f}')
print(f'Increased by 10%: R${coin.increase(price, 10 / 100):.2f}')
print(f'Decreased by 13%: R${coin.decrease(price, 13 / 100):.2f}')
