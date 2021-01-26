from old.fontefy import cabeçalho, cor
n1 = float(input('{}\n{:^40}\n{} \nDigite a nota do {}1°B _'.format(cabeçalho['line1'],'Calculo da média escolar',
                                                                    cabeçalho['line2'], cor['amarelo'])))
n2 = float(input('{}Digite a nota do {}2°B _{}'.format(cor['padrão'], cor['azul'], cor['padrão'])))
print('Sua {}média Semestral{} é igual a {}{:.1f}{}'.format(cor['verde'], cor['padrão'], cor['verde'], (n1 + n2) / 2,
                                                            cor['padrão']))
