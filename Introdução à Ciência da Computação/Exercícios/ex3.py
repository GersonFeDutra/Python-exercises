# -*- coding: utf-8 -*-
int_a = int(input('Digite um \033[34mnúmero inteiro:\033[m '))
int_b = int(input('Digite \033[35moutro número inteiro:\033[m '))
real = float(input('Digite um \033[36mnúmero real:\033[m '))

print('\nO\033[34m dobro do primeiro número\033[m vezes a'
        '\033[35m metade do segundo\033[m é: %s' % ((int_a * 2) * (int_b / 2)))
print('A soma do \033[34mtriplo do primeiro\033[m com o'
        '\033[36m terceiro\033[m é: %s' % ((int_a * 3) + real))
print('O\033[36m terceiro\033[m elevado ao cubo é: %s' % (real ** 3))
