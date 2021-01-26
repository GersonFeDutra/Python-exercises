"""By Misigno"""
cor = {'padrão': '\033[m', 'branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m',
        'azul': '\033[34m', 'roxo': '\033[35m','ciano': '\033[36m', 'cinza': '\033[37m'}
corB = {'padrão': '\033[m', 'branco': '\033[1;30m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m',
        'azul': '\033[1;34m', 'roxo': '\033[1;35m','ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
estilo = {'padrão': '\033[0m', 'negrito': '\033[1m', 'sublinhado': '\033[4m', 'negativo': '\033[7m',
          'marcado': '\033[1;30;43m', 'blueprint': '\033[1;30;44m', 'blueprint2': '\033[1;30;46m', 'dark': '\033[7;30m',
          'url': '\033[4;36m'}

cabeçalho = {'line1': '{}-{}='.format(cor['vermelho']*20, cor['amarelo'])*20+'{}'.format(estilo['negrito']),
             'line2': '{}-{}='.format(cor['verde'], cor['roxo'])*20+'{}'.format(cor['padrão']),
             'line3': '{}-{}='.format(cor['amarelo'], cor['azul']) * 20 + '{}'.format(cor['padrão'])}

is_presentable = False

class presentation():
    if is_presentable == True:
        print('{}Fontefy{} deixará{} o seu {}terminal{} mais {}b{}o{}n{}i{}t{}o{}!{}'.format(estilo['url'], cor['azul'],
                                                                                             cor['roxo'], estilo['dark'],
                                                                                             cor['verde'], cor['branco'],
                                                                                             cor['vermelho'], cor['verde'],
                                                                                             cor['amarelo'], cor['azul'],
                                                                                             cor['roxo'], cor['ciano'],
                                                                             cor['cinza']))