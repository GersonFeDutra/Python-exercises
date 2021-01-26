# -*- coding: utf-8 -*-
travel_time = (
    float(input('Digite uma distância qualquer de uma viagem (km): ')) / 
    float(input('Qual a velocidade média de locomoção (km/h): '))
) * 60 # Valor em minutos

print('O tempo de viajem estimado em horas é de %dh' % (travel_time // 60))
print('O tempo de viajem estimado em minutos é de %dm' % (travel_time % 60))
