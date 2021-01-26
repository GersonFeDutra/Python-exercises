# Tuplas
# São variáveis compostas imutáveis.
lanche: tuple = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(lanche[0]) # Will print "Hambúrguer"
print(lanche[1:3]) # Will print "('Suco', 'Pizza')"
print(lanche[-1]) # Will print "Pudim"
print(lanche[2:]) # Will print "('Pizza', 'Pudim')"
print(lanche[:2]) # Will print "('Hambúrguer', 'Suco')"
print(lanche[-2:]) # Will print "('Pizza', 'Pudim')"
print(lanche) # Will print ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#lanche[1] = 'Refrigerante' # A tupla não pode ser alterada!

for comida in lanche:
    print(f'Eu vou comer {comida}.')

print('Comi tudo!')

# O fluxo de repetição acima é equivalente à:
#for i in range(0, len(lanche)):
#    print(f'Eu vou comer {comida[i]}.')

# Note que i equivale a um índice da variável composta.
# Ela pode ser útil para obter a posição de um ítem durante a iteração.
# Uma forma alternativa de se fazer isso é por meio do método enumerate():

for i, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {i}.')


a: tuple = (2, 5, 4)
b: tuple = (5, 8, 1, 2)
c: tuple = b + a

# Métodos
print(sorted(lanche)) # Imprimirá a tupla de forma ordenada.
# Saída: "['Hambúrguer', 'Pizza', 'Pudim', 'Suco']"
print(len(lanche)) # Imprimirá o número de elementos na tupla.
# Saída: "4"
print(c.count(5)) # Imprimirá a quantidade de vezes que o elemento 5 aparece na tupla.
# Saída: "2"
print(c.count(9))
# Saída: "0"
print(c.index(8)) # Imprimirá o índice da primeira ocorrência de um elemento na tupla.
# Saída "1"
print(c.index(2))
# Saída "3"
print(c.index(2, 4)) # O segundo argumento indica o 'deslocamento' da posição inicial da busca.
# Saída "4"

# Concatenação
print(a + b) # Will print (2, 5, 4, 5, 8, 1, 2)
print(b + a) # Will print (5, 8, 1, 2, 2, 5, 4)

# Tuplas podem receber valores de diferentes tipos:
x: tuple = (0, 'Zero', 0.0, '0')

del(x) # Embora imutáveis, tuplas podem ser removidas da memória.
#print(x) # Logo, não poderá ser acessada posteriormente.
#del(a[0]) # Note que não é possível eliminar elementos individuais.
