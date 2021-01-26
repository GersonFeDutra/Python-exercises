phrase: str = input('Type a phrase: ').strip().upper()

print(f"""
The letter "A" appears {phrase.count('A')} times.
It appears the first time in the {phrase.find('A') + 1}° position.
It appears the last time in the {phrase.rfind('A') + 1}° position.""")
