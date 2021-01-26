from old.fontefy import corB, estilo
n = int(input('Digite um {}número inteiro{}: '.format(corB['branco'], corB['padrão'])))
suc = n + 1
ant = n - 1
print('.'*10, '{}{}{} < {}{}{} < {}{}{}'.format(corB['azul'], ant, corB['branco'], corB['amarelo'], n, corB['branco'],
                                                corB['ciano'], suc, corB['padrão']))
print('O {}antecessor{} de {}{}{} é {}{}{} e o seu {}sucessor{} é {}{}{}'.format(estilo['blueprint'], estilo['padrão'],
                                                                                 corB['amarelo'], n, corB['padrão'],
                                                                                 corB['azul'], ant, corB['padrão'],
                                                                                 estilo['blueprint2'], estilo['padrão'],
                                                                                 corB['ciano'], suc, corB['padrão']))
