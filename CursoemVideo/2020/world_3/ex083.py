# My solution
# chars: tuple = ('(', ')')
# parenthesis: list = []
# opened: int = 0
#
# for letter in input('Enter an arithmetic expression: '):
#     if letter in chars:
#         parenthesis.append(letter)
#
# for char in parenthesis:
#     if char == chars[0]:
#         opened += 1
#     else:
#         opened -= 1
#
#     if opened < 0:
#         break
#
# if opened == 0:
#     print('The expression is valid!')
# else:
#     print('The expression isn\'t valid!')

# Better solution
chars: tuple = ('(', ')')
stack: list = []
opened: int = 0

for letter in input('Enter an arithmetic expression: '):

    if letter == '(':
        stack.append('(')

    elif letter == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print('The expression is valid!')
else:
    print("The expression isn't valid!")
