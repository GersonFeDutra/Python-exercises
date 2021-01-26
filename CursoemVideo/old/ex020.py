from random import shuffle
from old.fontefy import cor, corB

n1 = input('Nome do {}primeiro {}aluno{}: '.format(cor['amarelo'], corB['amarelo'], corB['padrão']))
n2 = input('Nome do {}segundo {}aluno{}: '.format(cor['azul'], corB['azul'], corB['padrão']))
n3 = input('Nome do {}terceiro {}aluno{}: '.format(cor['vermelho'], corB['vermelho'], corB['padrão']))
n4 = input('Nome do {}quarto {}aluno{}: '.format(cor['ciano'], corB['ciano'], corB['padrão']))
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('Os {}alunos{} entregarão os exercícios na seguinte ordem:\n{}1° {}\n{}2° {}\n{}3° {}\n{}4° {}'.format(corB['branco'], corB['padrão'],
                                                                                                             cor['amarelo'], alunos[0],
                                                                                                             cor['azul'], alunos[1],
                                                                                                             cor['vermelho'], alunos[2],
                                                                                                             cor['ciano'], alunos[3]))

# My dumb method # (2020) -> Sério que eu fiz isso?????? :O :v
'''
r = random.choice(alunos)

print('Os alunos entregarão os exercícios na seguinte ordem:\n1° {}'.format(r))
alunos.remove(r)
r = random.choice(alunos)

print('2° {}'.format(r))
alunos.remove(r)
r = random.choice(alunos)

print('3° {}'.format(r))
alunos.remove(r)

print('4° {}'.format(alunos[0]))
'''
