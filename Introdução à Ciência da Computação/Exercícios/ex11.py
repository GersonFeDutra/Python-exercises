# -*- coding: utf-8 -*-
salary = float(input('Digite o valor do salário: R$ '))
percent = float(input('Digite o percentual de aumento: '))
increase = salary * percent / 100

print('\nO valor do aumento é de R$%.2f' % (increase))
print('\nO valor do novo salário após o aumento é de R$%.2f' % (salary + increase))
