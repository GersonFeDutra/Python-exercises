def counter(start: int, end: int, step: int) -> None:
    # Abaixo está a docstring da função.
    """
    Generates a counting.
    :param start: Where the counting starts.
    :param end: Where the counting ends.
    :param step: The step of the counting. Uses the absolute of the passed value.
    :return: None
    """
    count: int = start
    step = abs(step)
    sleep(.5)

    if step == 0:
        step = 1

    if start < end:
        while count <= end:
            print(count, end='')
            count += step
            print(end=(', ' if count <= end else '.'))
    else:
        while count >= end:
            print(count, end='')
            count -= step
            print(end=(', ' if count >= end else '.'))
            print()


help(counter)


def custom_sum(a: int, b: int, c: int = 0) -> None:
    """
    :param c: O parâmetro c é opcional. O seu valor padrão é 0.
    """
    print(a + b + c)


custom_sum(3, 2, 5)
custom_sum(8, 4) # c é passado como 0.
#custom_sum(8) # Essa chamada resulta em erro, pois a e b são obrigatórios.


def custom_multiply(a: int = 1, b: int = 1, c: int = 1) -> None:
    """
    Note que você pode ter todos os parâmetros como opcionais.
    """
    print(a * b * c)


custom_multiply(8, 2, 5)
custom_multiply(8, 4) # c é passado como 1
custom_multiply(8) # b e c são passados como 1
custom_multiply() # a, b e c são passados como 1


# Programa principal
n: float = 4.0
# Todas as propriedades declaradas fora de classes e funções em um script estão no escopo global do script, e podem ser acessadas nesse escopo e em todas as funções do script.
print(4)
del n
#print(n) # Exceto se a variável tiver sido deletada.
n = 4
print(n)


def any_func(x):
    # Todas as propriedades declaradas em uma função estão limitadas ao escopo dessa função e só podem ser acessadas por elas e todas as funções internas a essa.
    any_var = 2
    x += any_var + n # Note que você pode alterar o valor de um parâmetro sem ncessariamente alterar o valor do argumento passado.

    # Atenção! Embora seja possível acessar o valor de uma variável de escopo global do script,
    # Atribuir um valor a uma variável com o mesmo nome irá criar uma variável de escopo local da função.
    #n = n + 2 # Ao fazer isso a declaração acima não mais funcionará.
    
    print(x)
    print(any_var)
    print(n)


any_func(n)
#print(any_var) # Resulta em erro pois any_var não foi declarada no escopo global do script, embora declarado no escopo da função any_func()


def any_func2(x):
    global n # Para tratar a variável como a definida no escopo global, você pode usar a palavra-chave `global`.

    # Todas as propriedades declaradas em uma função estão limitadas ao escopo dessa função e só podem ser acessadas por elas e todas as funções internas a essa.
    any_var = 2
    x += any_var + n # Note que você pode alterar o valor de um parâmetro sem ncessariamente alterar o valor do argumento passado.
    n = n + 2 # Como n foi tratada como global, essa declaração funciona normalmente.
    
    print(x)
    print(any_var)
    print(n)


any_func2(n)


def grade_medium(a=0, b=0, c=0, d=0)  -> float:
    medium: float = (a + b + c + d) / 4
    #print(medium) # Você poderia usar o valor diretamente na função, mas retornar o valor permite uma maior flexibilidade.
    
    return medium # A palavra chave return permite passar um valor da função para a sua chamada.


answer: float = grade_medium(7, 6, 5, 9)  # Recebe o valor retornado por grade_medium().
print('Pupil 1:', answer)
print('Pupil 2:', grade_medium(6, 5, 8)) # Esse valor pode ser passado diretamente como argumento de uma outra chamada.


def show_year() -> None:
    # No Python, as importações podem ser feitas no escopo local de uma função.
    from datetime import date
    print(date.today().year)

show_year()
