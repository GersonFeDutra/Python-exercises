from old.fontefy import cor
d = float(input('Qual a {}distancia{} da viagem? {}Km_'.format(cor['azul'], cor['padrão'], cor['azul'])))
print('{}A viagem custará {}R${:.2f}'.format(cor['cinza'],cor['verde'], 0.50 * d if d <= 200 else 0.45 * d))
