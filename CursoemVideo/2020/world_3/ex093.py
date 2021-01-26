football_player: dict = {
    'name': input('Enter the football player data below_\nName: '),
    'matches': int(input('Matches played: ')),
    'goals': [],
    'score': 0
}
print('\nGoals in each match_')

for i in range(1, football_player['matches'] + 1):
    goals: int = int(input(f'{i}th math: '))
    football_player['goals'].append(goals)
    football_player['score'] += goals

print(football_player)

print(f'\nThe football player {football_player["name"]} played {football_player["matches"]} matches.')

for i, goals in enumerate(football_player['goals']):
    print(f'{"=>":>4} In the {i + 1}th match he did {goals} goals.')

print(f'He did a total of {football_player["score"]} goals.')
