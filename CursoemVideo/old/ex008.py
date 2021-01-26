m = float(input('Digite uma distancia em metros _'))
print('{}m equivalem à \n{}km (quilômetros)\n{}hm (hectômetros)\n{}dam (decâmetros)'.format(m, m/1000, m/100, m/10))
print('{}dm (decímetros)\n{:.0f}cm (centímetros)\n{:.0f}mm (milímetros)'.format(m*10, m*100, m*1000))
