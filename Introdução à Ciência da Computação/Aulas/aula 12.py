name = str(input('What is your name? ')).lower()

if name == 'linky':
    print('What a intriguishing name!')
    
elif name == 'irony' or name == 'luna' or name == 'lemug':
    print('Your name is really neat!')
    
elif name in 'ana cláudia jéssica juliana':
    print('Girl, you have an great name!')
    
else:
    print('What a boring name :|')

print('Have a good day', name.title())
