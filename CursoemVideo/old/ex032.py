from datetime import date
from old.fontefy import cor
ano = int(input('Escolha e digite um {}ano{} qualquer: '.format(cor['azul'], cor['padrão'])))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
