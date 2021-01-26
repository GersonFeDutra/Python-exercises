def push_message(message: str, size: int) -> None:
    print('-' * size)
    print(message.center(size))
    print('-' * size)

# All the calls below have the same output:
push_message('Python is awesome!', 20)
push_message(message='Python is awesome!', size=20)
push_message(size=20, message='Python is awesome!')
#push_message(size=20, 'Python is awesome!') # Note that you can't add an unamed arg after an explicitly named one.

# Python permite empacotar argumentos em um único parâmetro.
def counter(*numbers) -> int:
    print(len(numbers), 'values counted:', numbers)

    return sum(numbers)

print(counter(2, 1, 7))
print(counter(8, 0))
print(counter(4, 4, 7, 6, 2))
# Ambas as chamadas acima são válidas.

# Caso necessário o uso de arrays mutáveis (listas), você deverá passar uma lista de forma explícita.
def double(values: list) -> None:
    for i, value in enumerate(values):
        values[i] = value * 2

numbers: list = [5, 2, 5, 0, 4]
print(numbers)
double(numbers)
print(numbers)
