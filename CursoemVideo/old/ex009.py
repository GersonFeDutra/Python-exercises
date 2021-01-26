from old.fontefy import cabeçalho, cor
print('{}\n{:^40}\n{}'.format(cabeçalho['line1'], 'Tabuada eletrônica em python', cabeçalho['line2']))
n = int(input('Digite um número qualquer _'))

x = 0
while x < 10:
    x = x+1
    print('{} {}+{} {:>2} {}={} {}{}'.format(n, cor['azul'], cor['cinza'], x, cor['ciano'], cor['vermelho'], n + x, cor['padrão']))

print('#'*10)
x = 0
while x < 10:
    x = x+1
    print('{} {}-{} {:>2} {}={} {}{}'.format(n, cor['azul'], cor['cinza'], x, cor['ciano'], cor['vermelho'], n - x, cor['padrão']))

print('#'*10)
x = 0
while x < 10:
    x = x+1
    print('{} {}*{} {:>2} {}={} {}{}'.format(n, cor['azul'], cor['cinza'], x, cor['ciano'], cor['vermelho'], n * x, cor['padrão']))

print('#'*10)
x = 0
while x < 10:
    x = x + 1
    print('{} {}:{} {:>2} {}={} {:.1f}{}'.format(n, cor['azul'], cor['cinza'], x, cor['ciano'], cor['vermelho'], n / x, cor['padrão']))
