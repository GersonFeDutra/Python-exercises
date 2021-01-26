text: str = input('Enter an phrase: ').replace(' ', '').lower()

# length: int = len(text)
# is_palindrome: bool = True
#
# for i in range(0, length // 2):
#
#     if text[i] != text[length - 1 - i]:
#         is_palindrome = False
#         break
#
# print('\033[32mIs' if is_palindrome else '\033[31mIs not', 'a palindrome.\033[m')

# Using python slicing
print('\033[32mIs' if text == text[::-1] else '\033[31mIs not', 'a palindrome.\033[m')
