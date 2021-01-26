# -*- coding: utf-8 -*-

VICTORY_POINTS = 3
DRAW_POINTS = 1

cv = int(input('Digite abaixo os dados dos times.\n\nCormengo\n* Número de Vitórias: '))
ce = int(input('* Número de Empates: '))
cs = int(input('* Saldo de Gols: '))
cormengo = cv * VICTORY_POINTS + ce * DRAW_POINTS

fv = int(input('\nFlaminthians\n* Número de Vitórias: '))
fe = int(input('* Número de Empates: '))
fs = int(input('* Saldo de Gols: '))
flaminthians = fv * VICTORY_POINTS + fe * DRAW_POINTS

# Melhor classificado quem tem mais pontos
if cormengo > flaminthians:
    print('C')
    
elif cormengo < flaminthians:
    print('F')
    
# Em caso de empate no número de pontos, fica melhor classificado o time que tiver maior saldo de gols
elif cs > fs:
    print('C')
    
elif cs < fs:
    print('F')
    
# Se o número de pontos e o saldo de gols forem os mesmos para os dois times então ambos estarão empatados
else:
    print('=')

