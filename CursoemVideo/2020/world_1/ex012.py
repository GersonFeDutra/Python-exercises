DISCOUNT = 5 / 100
price: float = float(input('What is the product price? $'))

print(f'The product new price with 5% off is ${price - price * DISCOUNT :.2f}')
