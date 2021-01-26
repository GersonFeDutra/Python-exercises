from old.fontefy import cabeçalho, cor, estilo
print('{}\n{:^40}\n{}'.format(cabeçalho['line1'], 'Soma', cabeçalho['line2']))
n1 = int(input('Digite o {}primeiro número {}inteiro{}: '.format(cor['amarelo'], estilo['negrito'], estilo['padrão'])))
n2 = int(input('Digite o {}segundo número {}inteiro{}: '.format(cor['azul'], estilo['negrito'], estilo['padrão'])))
# print('a soma entre ', n1, ' e ', n2, ' vale ', s)
print('A {}soma{} entre {}{}{} e {}{}{} vale {}{}{}'.format(cor['verde'], cor['padrão'],
                                                            cor['amarelo'], n1, cor['padrão'],
                                                            cor['azul'], n2, cor['padrão'],
                                                            cor['verde'], n1 + n2, cor['padrão']))
