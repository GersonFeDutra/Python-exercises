import coin

price = float(input('Enter a price: R$'))
print(f'Half: {coin.coin(coin.half(price))}.')
print(f'Double: R${coin.coin(coin.double(price))}.')
print(f'Increased by 10%: {coin.coin(coin.increase(price, 10 / 100))}.')
print(f'Decreased by 13%: {coin.coin(coin.decrease(price, 13 / 100))}.')
