import coin

price = float(input('Enter a price: R$'))
print(f'Half: {coin.half(price)}.')
print(f'Double: R${coin.double(price, False)}.')
print(f'Increased by 10%: {coin.increase(price, 10 / 100, True)}.')
print(f'Decreased by 13%: {coin.decrease(price, 13 / 100, as_coin=True)}.')
