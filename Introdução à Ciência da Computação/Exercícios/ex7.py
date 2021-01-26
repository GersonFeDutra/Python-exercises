# -*- coding: utf-8 -*-
from math import pi, log10

g = 9.81
epsilon = 0.000002

f = float(input('Digite o valor de f: '))
L = float(input('Digite o valor de L: '))
Q = float(input('Digite o valor de Q: '))
delta_H = float(input('Digite o valor de delta H: '))
teta = float(input('Digite o valor de teta: '))

D = ((8 * f * L * (Q ** 2)) / ((pi ** 2) * g * delta_H)) ** (1 / 5)
Rey = (4 * Q) / (pi * D * teta)
k = (0.25) / (log10((epsilon / (3.7 * D)) + (5.47 / (Rey ** 0.9))) ** 2)

print('O valor de D é: %.4f' % D)
print('O valor de Rey é: %.4f' % Rey)
print('O valor de k é: %.4f' % k)
