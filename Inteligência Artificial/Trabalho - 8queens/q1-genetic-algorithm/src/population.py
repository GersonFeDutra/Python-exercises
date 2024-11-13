from math import ceil
from typing import Iterable
from random import randint, random
from .consts import *
from .individuals import Individual, IndividualFactory, RandomIndividualFactory


class Population():
    '''
    Representa a população do mini-verso do problema.

    @properties
        population:
            Um conjunto de indivíduos.
        generation:
            Geração atual (valor que será adicionado aos próximos indivíduos dessa geração).
            Isto é, a primeira geração terá indivíduos da "geração 0", e subsequentemente...
    '''
    population: list[Individual]
    generation: int = 0
    mutation_prob: float

    def show(self, h_set: int = 1) -> None:
        sp: list[int] = self.get_selection_probabilities()

        LINE_LEN: int = 20
        print('🌱' * LINE_LEN, f'{self.generation}° Geração', '🌱' * LINE_LEN)

        # Show individuals 1 by 1
        if h_set == 1:

            for i, individual in enumerate(self.population):
                print(f'{i + 1}° individual [{individual.id}]:')
                individual.show()
            return

        # Show individuals side by side, grouped in a number of `h_sets``
        size: int = len(self.population)
        for chunk in range(ceil(size / h_set)):
            offset: int = chunk * h_set
            print()

            for i in range(chunk * h_set, min(offset + h_set, size)):
                print(f'{i + 1}° individual:', end='\t\t')
            print()

            for i in range(chunk * h_set, min(offset + h_set, size)):
                print(f'{self.population[i]}, sp:{(sp[i] * 100):.0f}%', end='\t')
            print()

            for row in range(TABLE_SIZE):
                for i in range(h_set):
                    if offset + i >= size:
                        break

                    self.population[offset + i].show_row(row)
                    print(end='\t')
                print()

    def select(self) -> tuple:
        '''Seleciona os próximos pais, com base em um contador interno.
            O contador é "resetado" quando a população avançar para a próxima geração.'''
        last: int = self._selection_pointer
        self._selection_pointer -= 1
        return (self.population[last], self.population[self._selection_pointer])

    def crossover(self, a: Individual, b: Individual) -> tuple:
        '''
        Realiza a operação de crossover entre os indivíduos A e B.

        Retorna uma tupla com os filhos gerados.
        '''
        OFFSET: int = 1
        TABLE_MAX_INDEX: int = TABLE_SIZE - 1
        seed: int = randint(OFFSET, TABLE_MAX_INDEX - OFFSET)
        child_dna_a: list[int] = []
        child_dna_b: list[int] = []

        for i in range(seed):
            child_dna_a.append(a.dna[i])
            child_dna_b.append(b.dna[i])

        for i in range(seed, TABLE_SIZE):
            child_dna_a.append(b.dna[i])
            child_dna_b.append(a.dna[i])

        if random() > self.mutation_prob:
            child_dna_a[randint(OFFSET, TABLE_MAX_INDEX)] = randint(OFFSET, TABLE_MAX_INDEX)

        return (Individual(child_dna_a, self.generation), Individual(child_dna_b, self.generation))

    def get_selection_probabilities(self) -> list[int]:
        '''Gera um vetor de probabilidades com base no fitness de cada indivíduo da população.'''
        if self._total_adaptability <= 0:
            return [0] * len(self.population)

        probabilities: list[int] = []

        # Gera a probabilidade com base no total de adaptabilidade de toda a população.
        for individual in self.population:
            probabilities.append(individual.get_fitness() / self._total_adaptability)

        return probabilities

    def sort(self) -> None:
        '''Ordena a população com base nos indivíduos que estão melhor adaptados.
            Aqueles com o maior valor de fitness aparecerão por último na lista.'''
        self.population.sort(key=lambda x: x.get_fitness())

    def add(self, it: Iterable) -> None:
        self.population.extend(it)
        self.sort()

    def next(self, pop_size: int) -> None:
        '''"Evolui" a população para a próxima geração.'''
        # Mantém os indivíduos mais adaptados na população
        self.population = self.population[len(self.population) - pop_size:]
        self.generation += 1
        self._selection_pointer = pop_size - 1

    def best(self):
        '''Returns the best individual of the current population.'''
        return self.population[-1] # Assumindo que o vetor está ordenado.

    def __init__(self, population_size: int, mutation_probability: float = 0.0,
            factory: IndividualFactory = RandomIndividualFactory) -> None:
        self.population = list()
        # O total de "adaptação" da população.
        # Obtido pela soma do `fitness` de cada indivíduo da população.
        self._total_adaptability: int = 0
        self._selection_pointer: int = population_size - 1
        self.mutation_prob = mutation_probability

        for _ in range(population_size):
            new: Individual = factory.create()
            self.population.append(new)
            self._total_adaptability += new.get_fitness()

        self.sort()
        self.generation += 1
