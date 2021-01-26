products = {
    "Parafusos": 10,
    "Porcas": 5
}
line_sizing = 15

def title(message):
    print('\33[00m\33[31m{}\33[00m'.format(message))

title("{} Loginha do seu cadú {}".format("=" * line_sizing, "=" * line_sizing))

def cost(product, price):
    print("{} custam {:.2f} R$".format(product, price))

for product in products:
    cost(product, products[product])

title("-" * (line_sizing * 2 + line_sizing))

def qtd(product):
    return int(input("Quantos {}, você quer?".format(product)))

products_qtds = products

for product in products_qtds:
    products_qtds[product] = qtd(product)

print("Você comprou:")

def result(qtd, name, price):
    print("{} {} por {} R$".format(qtd, name, qtd * price))

for product in products:
    result(products_qtds[product], product.lower(), products[product])
