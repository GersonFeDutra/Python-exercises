words: tuple = ('learn', 'program', 'python', 'course', 'study', 'practice', 'work', 'market', 'programmer', 'future')

for word in words:
    word = word
    total: int = 0
    word_vowels: str = ''

    for letter in word:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            total += 1
            word_vowels += letter

    print(f'The word {word.upper()} has {total} vowels ' + (f'({word_vowels}).' if len(word_vowels) > 0 else "."))
