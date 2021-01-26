name: str = input('Enter a full name? ').strip()

# print('You have "Silva" in your name?', "silva" in name.lower())
print('You have "Silva" in your name?', "silva" in name.lower().split())  # Smarter :3
