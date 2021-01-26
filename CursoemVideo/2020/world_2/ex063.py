"""
Fibonacci
"""
n_terms: int = int(input('How many terms in the Fibonacci sequence do you want to see? '))
fibonacci: int = 0
last_value: int = 1

while n_terms > 0:

    print(fibonacci)
    fibonacci += last_value
    last_value = fibonacci - last_value
    n_terms -= 1
