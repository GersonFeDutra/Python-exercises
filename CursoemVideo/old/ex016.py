from math import hypot
from old.fontefy import cor
co = float(input('Comprimento do {}cateto oposto{}: '.format(cor['azul'], cor['padrão'])))
ca = float(input('Comprimento do {}cateto adjacente{}: '.format(cor['vermelho'], cor['padrão'])))
print('A {}hipotenusa{} vai medir {}{:.2f}{}'.format(cor['roxo'], cor['padrão'], cor['roxo'], hypot(co, ca), cor['padrão']))
