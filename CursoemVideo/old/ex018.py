from old.fontefy import cor
from math import tan, cos, sin, radians
aRad = radians(float(input('Digite o valor de um {}ângulo °'.format(cor['ciano']))))
print('{}Seno = {:.3f}\n{}Cosseno = {:.3f}{}\nTangente = {:.3f}'.format(cor['amarelo'], sin(aRad), cor['verde'], cos(aRad), cor['roxo'], tan(aRad)))
