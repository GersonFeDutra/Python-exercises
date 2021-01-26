from old.fontefy import cor
c = input('Digite o nome de uma {}cidade{}: '.format(cor['branco'], cor['padrão'])).strip()

""" My Dumb Way"""
#cpn = c.split()[0]
#print('A cidade {} começa com o nome SANTO: {}'.format(c, 'santo' in cpn.lower()))

print('{} {}Santo{} no início!'.format('{}Há'.format(cor['verde']) if c[:5].upper() == 'SANTO' else '{}Não Há'.format(cor['vermelho']), cor['roxo'], cor['padrão']))
