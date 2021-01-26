from old.fontefy import cor
v = int(input('Qual a {}velocidade{} do carro? {}Km/h_'.format(cor['azul'], cor['padrão'], cor['azul'])))
print('{}Este carro será multado em {}R${:.2f}!'.format(cor['vermelho'], cor['verde'], (v-80)*7) if v > 80
      else '{}O carro está dentro do limite!'.format(cor['verde']))
