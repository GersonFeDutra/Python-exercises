# Listas
#num: tuple = (2, 5, 9, 1)
#num[2] = 3 # Tuplas são imutáveis e não podem ser atribuidas.
num: list = [2, 5, 9, 1]
num[2] = 3 # Já arrays podem ser alterados livremente.
print(num) # Saída: [2, 5, 3, 1]
#num[4] = 7 # Porém não é possível atribuir valores à índices inexistentes.

# Para adicionar elementos você pode usar os métodos abaixo:
num.append(7) # O método append() adiciona elementos no final do array.
print(num) # Saída: [2, 5, 3, 1, 7]
num.insert(3, 2) # Adiciona elementos na posição(índice/ chave) indicado.
print(num) # Saída: [2, 5, 3, 2, 1, 7]

# Para remover elementos você pode usar os métodos abaixo:
num.pop() # Remove o último elemento do array.
print(num) # Saída: [2, 5, 3, 2, 1]
num.pop(1) # Opcionalmente você pode passar um índice para o método pop.
print(num) # Saída: [2, 3, 2, 1]
num.remove(2) # Remove a primeira ocorrência do elemento indicado.
print(num) # Saída: [3, 2, 1]
# Por segurança você pode adicionar uma verificação:
if 4 in num:
    num.remove(4) # Sem a verificação, o interpretador dispararia um erro, pois a chave 4 não existe nesse array.

num.sort() # Irá organizar os valores do array em ordem crescente.
print(num) # Saída: [1, 2, 3]
num.sort(reverse=True) # Irá organizar os valores do array em ordem decrescente.
print(num) # Saída: [3, 2, 1]

print(len(num)) # Imprime o número de elementos no array.
# Saída: 3

valores: list = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores) # Saída: [5, 9, 4]

# Iterando:

for valor in valores:
    print(f'{valor}...', end=' ')
print()
# Saída: 5... 9... 4...

for chave, valor in enumerate(valores):
    print(f'No índice {chave} há o valor {valor}.')
# Saída:
"""No índice 0 há o valor 5.
No índice 1 há o valor 9.
No índice 2 há o valor 4.
"""

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um número inteiro: ')))
# Irá dar entrada há 5 valores na lista.

# Observação: listas são compartilhadas entre instâncias (passadas por referência).
a: list = [2, 3, 4, 7]
b: list = a
b[2] = 8
print('a =', a) # Saída: a = [2, 3, 8, 7]
print('b =', b) # Saída: b = [2, 3, 8, 7]

# Para fazer uma cópia de uma lista, você pode usar o fatiamento:
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print('a =', a) # Saída: a = [2, 3, 4, 7]
print('b =', b) # Saída: b = [2, 3, 8, 7]
