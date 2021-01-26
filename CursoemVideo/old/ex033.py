from old.fontefy import cor
n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
menor = n1
maior = n3
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
print('O {}menor{} número é {}{}{} e o {}maior{} é {}{}{}'.format(cor['vermelho'], cor['padrão'], cor['vermelho'],
                                                                  menor, cor['padrão'], cor['azul'], cor['padrão'],
                                                                  cor['azul'], maior, cor['padrão']))

""" My hyper dumb Way 
if n1 > n2:
    if n1 > n3:
        p1 = n1 #n1 na primeira posição
        if n2 > n3:
            p2 = n2
            p3 = n3
        else:
            p2 = n3
            p3 = n2
    else:
        p2 = n1 #n1 na segunda posição
        if n2 > n3:
            p1 = n2
            p3 = n3
        else:
            p1 = n3
            p3 = n2
else:
    if n1 < n3:
        p3 = n1 #n1 na terceira posição
        if n2 > n3:
            p1 = n2
            p2 = n3
        else:
            p1 = n3
            p2 = n2
    else:
        p2 = n1 #n1 na segunda posição
        if n2 > n3:
            p1 = n2
            p3 = n3
        else:
            p1 = n3
            p3 = n2
print('{} >= {} >= {}'.format(p1, p2, p3))
"""
