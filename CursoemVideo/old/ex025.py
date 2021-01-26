from old.fontefy import cor, cabeçalho
print('{}\n{:^40}\n{}'.format(cabeçalho['line1'], 'Você é quem estou procurando?!', cabeçalho['line2']))
n = input('Digite seu {}nome completo{}: '.format(cor['branco'], cor['padrão']))
print('{}Você é SILVA'.format(cor['verde']) if 'silva' in n.lower() else '{}Você não é SILVA'.format(cor['vermelho']))
