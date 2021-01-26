from old.fontefy import cor
l = float(input('Qual a {}largura{} da parede? '.format(cor['azul'], cor['padrão'])))
h = float(input('Qual a {}altura{} da parede? '.format(cor['ciano'], cor['padrão'])))
a = l*h
print('Com uma parede {}{:.0f}{}x{}{:.0f}{} de {}{:.1f}m²{} será nesseçário {}{:.3f} litros{} de tinta para pintá-la'.format(cor['azul'], l, cor['cinza'],
                                                                                                                     cor['ciano'], h, cor['padrão'],
                                                                                                                     cor['vermelho'], a, cor['padrão'],
                                                                                                                     cor['branco'], a / 2, cor['padrão']))
