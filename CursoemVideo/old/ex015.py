from old.fontefy import cor
d = int(input('Por quantos {}dias{} o carro foi alugado? _'.format(cor['azul'], cor['padrão'])))
q = int(input('Quantos {}quilômetros{} o carro percorreu? {}Km_{}'.format(cor['amarelo'], cor['padrão'], cor['amarelo'], cor['padrão'])))
print('Você terá que pagar {}R${:.2f}{} pelo aluguel do carro!'.format(cor['verde'] ,d * 60 + q * 0.15, cor['padrão']))
