pessoas: dict = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys()) # dict_keys(['nome', 'sexo', 'idade']
print(pessoas.values()) # dict_values(['Gustavo', 'M', 22)
print(pessoas.items()) # dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])

for key in pessoas.keys():
    print(key)

for value in pessoas.values():
    print(value)

for key, value in pessoas.items():
    print(f'{key} = {value}')

del pessoas['sexo'] # Remove uma entrada do dicionário
#print(pessoas['sexo']) # Acessar o valor removido resulta em erro

pessoas['nome'] = 'Leandro'
print(pessoas['nome']) # Output: Leandro

pessoas['peso'] = 98.5 # Adiciona uma nova entrada no dicionário
print(pessoas)

# Estruturas multidimensionadas:
estados = [
    {'uf': 'Rio de Janeiro', 'sigla': 'RJ'},
    {'uf': 'São Paulo', 'sigla': 'SP'}
]
print(estados) # Output: [Rio de Janeiro', 'sigla': 'RJ'}, São Paulo', 'sigla': 'SP'}]
estados[1] # Output: {'uf': 'São Paulo', 'sigla': 'SP'}
print(estados[0]['uf']) # Output: Rio de Janeiro

novo_estado: dict = {}

for i in range(3):
    novo_estado['uf'] = input('Unidade Federativa: ')
    novo_estado['sigla'] = input('Sigla do Estado: ')
    #estados.append(estado) # Dicionários são passados por referência.
    estados.append(novo_estado.copy()) # Se eles não forem copiados eles serão compartilhados entre instâncias.

print(estados)

for i, estado in enumerate(estados):
    print(f'{i + 1}°', end=' ')
    
    for key, value in estado.items():
        print(f'{key}: {value}', end=' ')
    print()
