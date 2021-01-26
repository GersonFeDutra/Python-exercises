from random import randint
from time import sleep
from old.fontefy import cabeçalho, corB
r = randint(0, 5)
print('{}\n{:^40}\n{}'.format(cabeçalho['line1'], 'Pensei em um número entre 0 e 5!', cabeçalho['line2']))
n = int(input('Qual {}número{} foi escolhido? '.format(corB['cinza'], corB['padrão'])))
print('{:^40}'.format('PROCESSANDO'))
sleep(1)
print(cabeçalho['line3'])
sleep(1)
print(cabeçalho['line2'])
sleep(1)
print(cabeçalho['line1'], corB['padrão'])

print('O número escolhido foi {}.'.format(r),
      '{}Você acertou!'.format(corB['verde']) if n == r else '{}Você errou!'.format(corB['vermelho']))
