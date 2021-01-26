from random import choice
from old.fontefy import cabeçalho, cor, estilo
print('{}\n{:^40}\n{}'.format(cabeçalho['line2'], 'Sorteando aluno para apagar a lousa', cabeçalho['line1']))
n1 = input('Digite o nome do {}primeiro {}aluno{}: '.format(cor['amarelo'], estilo['negrito'], cor['padrão']))
n2 = input('Digite o nome do {}segundo {}aluno{}: '.format(cor['azul'], estilo['negrito'], cor['padrão']))
n3 = input('Digite o nome do {}terceiro {}aluno{}: '.format(cor['vermelho'], estilo['negrito'], cor['padrão']))
n4 = input('Digite o nome do {}quarto {}aluno{}: '.format(cor['ciano'], estilo['negrito'], cor['padrão']))
alunos = [n1, n2, n3, n4]
print('Entre {}{}, {}{}, {}{} e {}{}; {}o aluno escolhido{} foi {}{}.'.format(cor['amarelo'], n1, cor['azul'], n2,
                                                                              cor['vermelho'], n3, cor['ciano'], n4,
                                                                              estilo['negrito'], estilo['padrão'],
                                                                              cor['branco'], choice(alunos)))
