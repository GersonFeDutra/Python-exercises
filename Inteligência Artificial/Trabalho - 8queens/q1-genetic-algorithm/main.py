from sys import argv, stderr, exit
from typing import Tuple
from src.population import Population
from src.individuals import Individual, BaseIndividualFactory, max_clashes

NONE_CALL = lambda *args: None
columns: int = 1


def ui(population: Population) -> None:
    '''Apresenta uma "interface do usuário" em torno do algoritmo genético.'''
    global columns

    population.show(columns)
    # print('What to do next? Enter (go to next generation):', end=' ')
    print('Press Enter (go to next generation):', end=' ')

    try:
        input()
    except EOFError:
        exit()

    return


def genetic_algorithm(pop_size: int, it_max: int, mut_prob: float) -> None:
    '''
    Algoritmo genético para o problema das 8 rainhas.
    A população é evoluída de forma elitista: em que a população da próxima iteração é
    composta pelos `n` melhores indivíduos da população atual, tal que `n = pop_size`.

    @args
        pop_size: tamanho da população;
        it_max: número máximo de iterações que irá executar;
        mut_prob: a taxa de probabilidade de mutação.
    '''
    population = Population(pop_size, mut_prob)
    ui(population)

    while population.generation <= it_max and population.best().get_fitness() < max_clashes:
        new: list[int] = []

        for i in range(pop_size):
            parents: tuple[Individual] = population.select()
            children: tuple[Individual] = population.crossover(*parents)
            # A mutação é feita internamente no crossover.
            new.extend(children)

        population.add(new)
        population.next(pop_size)
        ui(population)

    population.best().show()


def main(pop_size: int = 8, cols: int = 4, skip_generations: bool = False) -> None:
    global columns
    global ui

    if skip_generations:
        ui = NONE_CALL
    else:

        print('Show generations? (Y/n)', end=' ')
        try:
            if input().lower().startswith('n'):
                ui = NONE_CALL
        except EOFError:
            exit()

    # population = Population(8, BaseIndividualFactory())
    # population.show(columns)
    columns = cols
    genetic_algorithm(pop_size, 10, 1 / pop_size)
    # Um em cada 'n' indivíduos gerados sofrerão mutação.


if __name__ == '__main__':
    args: list[str] = [] # Ignora os argumentos adicionais.
    kwargs: dict[str, Tuple[int, bool]] = {}
    skip: bool = False
    use_default: bool = False

    for i, arg in enumerate(argv):
        if skip:
            skip = False
            continue

        try:
            match arg:
                case '-':
                    use_default = True
                case '-popsize':
                    kwargs['pop_size'] = int(argv[i + 1])
                    skip = True
                case '-cols':
                    kwargs['cols'] = int(argv[i + 1])
                    skip = True
                case '-skip':
                    kwargs['skip_generations'] = True
                case _:
                    args.append(argv[i])
        except (IndexError, ValueError) as e:
            print(e, file=stderr)

    # print(*args)

    if use_default:
        main(**kwargs)
    else:
        # Realiza as execuções pedidas no exercício.
        print('Pick some running option:')
        print('1 - run 10x a population with 150 individuals (skip generations).')
        print('2 - run 10x a population with 100 individuals (skip generations).')
        print('3 - run 10x a population with 200 individuals (skip generations).')
        print('\033[34m0 - use default.\033[m')
        print('\033[32m>>>\033[m', end=' ')
        pop_size: int = 0

        try:
            match int(input()):
                case 1:
                    pop_size = 150
                case 2:
                    pop_size = 100
                case 3:
                    pop_size = 200
                case _:
                    use_default = True
        except EOFError:
            exit()
        except ValueError:
            use_default = True

        if use_default:
            main(**kwargs)
        else:
            ui = NONE_CALL
            for i in range(10):
                print(f'\n{i + 1}° Execução:')
                genetic_algorithm(pop_size, 100, 0.2)
