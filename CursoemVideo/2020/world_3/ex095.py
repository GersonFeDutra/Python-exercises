# ex093 updated
football_players: list = []


def get_from_options(options: tuple, message: str) -> str:
    option: str = ''

    while option not in options:
        option = input(message).lower()

    return option


while True:

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

    football_players.append(football_player)
    print('⚽' * 20)

    if get_from_options(('y', 'n'), 'Do you want to continue? ') == 'n':
        break

print(f'\nid {"name":10} {"goals":10} total')

for i, football_player in enumerate(football_players):

    print(f'{i:>2} {football_player["name"]:10} {str(football_player["goals"]):10} {football_player["score"]:<5}')

while True:
    answer: int = int(input('\nDo you wan to see data from which player? (-1 to none) '))
    football_player: dict

    if answer < 0:
        break

    if answer >= len(football_players):
        print("\033[31m⚠ Error! There are no entries with this id. Try Again...\033[m")
        continue

    football_player = football_players[answer]
    for j, goals in enumerate(football_player['goals']):
        print(f'{"=>":>4} In the {j + 1}th match {football_player["name"]} did {goals} goals.')

    print(f'He did a total of {football_players[answer]["score"]} goals.')
