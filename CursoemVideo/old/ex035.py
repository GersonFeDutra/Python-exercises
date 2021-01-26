from old.fontefy import cor, estilo
print('{}-{}='.format(cor['verde'], cor['roxo'])*20, '\n{}{:^40}'.format(estilo['negrito'], 'Analizador de triangulos'))
print('{}-{}='.format(cor['ciano'], cor['vermelho'])*20, '{}'.format(cor['padrão']))
l1 = float(input('Qual o tamanho da {}primeira{} reta? '.format(cor['amarelo'], cor['padrão'])))
l2 = float(input('Qual o tamanho da {}segunda{} reta? '.format(cor['azul'], cor['padrão'])))
l3 = float(input('Qual o tamanho da {}terceira{} reta? '.format(cor['vermelho'], cor['padrão'])))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('{}É possível{} formar triangulo'.format(estilo['sublinhado'], estilo['padrão']))
else:
    print('{}Não é possível{} formar um triangulo'.format(estilo['sublinhado'], estilo['padrão']))

""" My dumb Way
ms1 = '{}É possível{} formar triangulo'.format(estilo['sublinhado'], estilo['padrão'])
ms2 = '{}Não é possível{} formar um triangulo'.format(estilo['sublinhado'], estilo['padrão'])

if l1 >= l2 >= l3:
    print(ms1 if l2 + l3 >= l1 else ms2)
    #l1
else:
    if l2 >= l3:
        print(ms1 if l1 + l3 >= l2 else ms2)
        #l2
    else:
        print(ms1 if l1 + l2 >= l3 else ms2)
        #l3
"""