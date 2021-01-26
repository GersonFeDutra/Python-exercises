placing: tuple = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo', 'Internacional',
                  'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético', 'Fluminense', 'Botafogo',
                  'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print('List of teams from the Brasileirão:', placing)
print(f'First 5 places:', placing[:5])
print(f'Last 4 places:', placing[-4:])
print(f'In order:', sorted(placing))
print(f'Chapecoense is in {placing.index("Chapecoense") + 1}th place.')
