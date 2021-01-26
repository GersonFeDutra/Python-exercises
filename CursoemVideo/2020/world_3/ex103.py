def token(name: str = '', goals: int = 0) -> None:
    print(f'The player {name if name else "<unknown>":} did {goals} goals in the championship.')


player_name: str = input('Name of the football player: ').strip()
player_goals: str = input('Total of goals: ')

if player_goals.isnumeric():
    token(player_name, int(player_goals))
else:
    token(player_name)
