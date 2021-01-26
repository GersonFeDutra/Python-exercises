from old.fontefy import cabeçalho, estilo, cor

print('{}\n{:^40}\n{}'.format(cabeçalho['line1'], 'Analizador de String', cabeçalho['line2']))
valor = input('Digite algo: ')

print('A {}{}{} {}{}{}...'.format(estilo['negrito'], type(valor), estilo['padrão'], estilo['negativo'], valor, estilo['padrão']))
positivo = '{}É'.format(cor['verde'])
negativo = '{}Não é'.format(cor['vermelho'])
print('{} Alfanumerico'.format(positivo if valor.isalnum() else negativo))
print('{} Alfabético'.format(positivo if valor.isalpha() else negativo))
print('{} Decimal'.format(positivo if valor.isdecimal() else negativo))
print('{} Digito'.format(positivo if valor.isdigit() else negativo))
print('{} Indentificavel'.format(positivo if valor.isidentifier() else negativo))
print('{} Minusculo'.format(positivo if valor.islower() else negativo))
print('{} Numerico'.format(positivo if valor.isnumeric() else negativo))
print('{} Printavel'.format(positivo if valor.isprintable() else negativo))
print('{} Espaço'.format(positivo if valor.isspace() else negativo))
print('{} Titulo'.format(positivo if valor.istitle()else negativo))
print('{} Maiusculo'.format(positivo if valor.isupper() else negativo))
