from old.fontefy import corB
n = input('Digite o seu {}nome completo{}: '.format(corB['branco'], corB['padrão'])).strip()
print('{}Muito prazer em te conhecer!{}'.format(corB['verde'], corB['padrão']))
print('Seu {}primeiro nome{} é:{} {}\n{}Seu {}último nome{} é: {}{}'.format(corB['amarelo'], corB['padrão'],
                                                                          corB['amarelo'], n[:n.find(' ')], corB['padrão'],
                                                                          corB['roxo'], corB['padrão'],
                                                                          corB['roxo'], n[n.rfind(' ') + 1:]))

""" Guanabara Dumb Way """
#nome = n.split()
#print('Muito prazer em te conhecer!')
#print('Seu primeiro nome é {}\nSeu segundo nome é {}'.format(nome[0], nome[len(nome) - 1]))
