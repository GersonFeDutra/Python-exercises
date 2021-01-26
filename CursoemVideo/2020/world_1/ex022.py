name: str = input('Enter your full name: ').strip()

print(f"Upper-case: {name.upper()}")
print(f"Lower-case: {name.lower()}")
print(f"Number of characters (without spaces): {len(name) - name.count(' ')}")  # Outra forma de resolver: len(name.replace(' ', ''))
print(f"Number of characters in the first name: {len(name.split()[0])}")  # Outra forma de resolver: name.find(' ') (não funciona como um nome único
