from old.fontefy import corB
n = int(input('Digite um {}número inteiro{}: '.format(corB['branco'], corB['padrão'])))
print('O {}dobro{} de {}{}{} é {}{}{}, o {}triplo{} é {}{}{} e sua {}raiz{} é {}{:.3f}{}'.format(corB['azul'], corB['padrão'],
                                                                                             corB['branco'], n, corB['padrão'],
                                                                                             corB['azul'], n * 2, corB['padrão'],
                                                                                             corB['ciano'], corB['padrão'],
                                                                                             corB['ciano'], n *3, corB['padrão'],
                                                                                             corB['amarelo'], corB['padrão'],
                                                                                             corB['amarelo'], n ** (1 / 2), corB['padrão']))
