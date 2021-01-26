from old.fontefy import estilo
s = float(input('Qual o seu salário? '))
print('Seu novo salário é de {}R${:.2f}{}'.format(estilo['negrito'],
                                                  s + (s * 10 /100) if s > 1250 else s + (s * 15 / 100),
                                                  estilo['padrão']))
