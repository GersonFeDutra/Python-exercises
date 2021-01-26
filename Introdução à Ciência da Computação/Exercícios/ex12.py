# -*- coding: utf-8 -*-
price = float(input('Digite o valor de um produto: R$ '))
discount = price * float(input('Qual o percentual de disconto? ')) / 100

print('O valor do desconto é de R$ %.2f' % discount)
print('O valor do produto após o desconto é de R$ %.2f' % (price - discount))
