from old.fontefy import cor
n = int(input('Digite um número de {}0 a 9999{}: '.format(cor['branco'], cor['padrão'])))

"""Formatação por String"""
#nS = '{:>4}'.format(n).replace(' ', '0')
#print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(nS[3], nS[2], nS[1], nS[0]))

"""Formatação Matemática"""
unidade = n % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
print('{}Unidade: {}'.format(cor['amarelo'], unidade))
if dezena != 0:
    print('{}Dezena: {}'.format(cor['verde'], dezena))
    if centena != 0:
        print('{}Centena: {}'.format(cor['azul'], centena))
        if milhar != 0:
            print('{}Milhar: {}'.format(cor['vermelho'], milhar))
