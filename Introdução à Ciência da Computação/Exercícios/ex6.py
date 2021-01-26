# -*- coding: utf-8 -*-
a = float(input('Digite o coeficiente\033[34m a\033[m de uma equação de segundo grau: '))
b = float(input('Digite agora o coeficiente\033[34m b\033[m: '))
c = float(input('Por fim, digite o coeficiente\033[34m c\033[m: '))
delta_root = (b ** 2 - 4 * a * c) ** 0.5
double_a = 2 * a

print('Dado os coeficientes acima, as raízes da equação são:'
    '\nx1 = %s' % ((-b + delta_root) / double_a))
print('x2 =', (-b - delta_root) / double_a)
