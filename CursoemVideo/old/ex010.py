from old.fontefy import corB, cabeçalho
r = float(input('{}\n{:^40}\n{}\nQuanto {}dinheiro{} você tem na carteira? {}_R${}'.format(cabeçalho['line1'],
                                                                                       'Conversor de Moeda',
                                                                                       cabeçalho['line2'],
                                                                                       corB['verde'], corB['padrão'],
                                                                                       corB['verde'], corB['padrão'])))
print('Você pode comprar {}{:.2f}US${}, com esta quantia!!'.format(corB['verde'], r / 3.27, corB['padrão']))
