from old.fontefy import corB
f = input('Digite uma frase: ').strip().upper()
print('A {}letra A{} aparece {}{} vezes{} na frase digitada.'.format(corB['branco'], corB['padrão'], corB['roxo'],
                                                                     f.upper().count('A'), corB['padrão']))
aPosition = f.find('A')
a1 = aPosition + 1
a2 = f.find('A', aPosition + 1) + 1
if a1 != 0:
    print('A {}primeira letra A{} aparece na {}{}° posição{}'.format(corB['amarelo'], corB['padrão'],
                                                                     corB['branco'], a1, corB['padrão']))
    if a2 != 0:
        print('A {}segunda letra A{} aparece na {}{}° posição{}'.format(corB['verde'], corB['padrão'],
                                                                        corB['branco'], a2, corB['padrão']))
    print('A {}última letra A{} aparece na {}{}° posição{}'.format(corB['vermelho'], corB['padrão'],
                                                                   corB['branco'], f.rfind('A') + 1, corB['padrão']))
