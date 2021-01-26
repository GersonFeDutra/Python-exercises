from old.fontefy import cor
nome = input('Digite o seu {}nome completo{}: '.format(cor['branco'], cor['padrão'])).strip()
print(cor['branco'], nome.upper(), '\n', cor['cinza'], nome.lower(), cor['padrão'])

'''    My dumb Way
nomeSemSpc = nome.split()
pn = nomeSemSpc[0]
nomeSemSpc = ''.join(nomeSemSpc)
print('Seu nome tem {} caracteres'.format(len(nomeSemSpc)))
print('O seu 1° nome tem {} caracteres'.format(pn.__len__()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
'''

#   My non dumb Way
print('O seu {}primeiro nome{} tem {}{} letras'.format(cor['amarelo'], cor['padrão'], cor['vermelho'],
                                                         len(nome.split()[0])))

#print('O seu {}primeiro nome{} tem {}{} letras{}'.format(cor['amarelo'], cor['padrão'], cor['vermelho'], nome.find(' '), cor['padrão']))
