from numpy import unique
from random import randint
from .consts import TABLE_SIZE

# Campo estático usado para obter identificadores únicos.
current_id: int = 0
def next_id() -> int:
    global current_id
    id = current_id
    current_id += 1

    return id


max_clashes: int = 0 # Maximum number of clashes
for i in range(1, TABLE_SIZE):
    max_clashes += i


class Individual():
    '''
    Um indivíduo de uma população.
    Representa uma rainha no problema das 8 rainhas.

    @properties
        dna:
            Cada posição na tupla `dna` representará a coluna que a rainha será posicionada.
            Enquanto que o valor dado naquela posição indica a linha.
        generation:
            Em que geração esse indivíduo foi gerado.
        id:
            Identificador único do indivíduo.

    @methods
        get_fitness():
            O valor de adaptação do indivíduo.
    '''
    dna: tuple[int] # Definido como tupla, pois o dna deve ser fixo para cada indivíduo.
    generation: int 
    id: int

    def show(self) -> None:
        print(f'{self}')

        for row in range(TABLE_SIZE):
            self.show_row(row)
            print()

        print(f'gen:{self.generation}, dna:{self.dna}')

    def show_row(self, row) -> None:

        for col in range(TABLE_SIZE):
            print(f'{("👑" if self.get_row(col) == row else ( "⬛" if (row + (col % 2)) % 2 == 0 else "⬜")):^1s}', end='')

    def _get_fitness(self) -> int:
        '''
        Calcula o fitness do indivíduo em `O(n)`,
        onde `n` é o tamanho (medido em quadrados) de um lado do tabuleiro.
        '''
        clashes: int = 0 # row clashes + right diagonal clashes + left diagonal clashes

        higher_index = TABLE_SIZE - 1
        # Rainhas em cada coluna
        row_queens: list[int] = [0] * TABLE_SIZE
        # O índice da última diagonal em uma direção calculado por (n - 1) * 2 - 2 + 1.
        d: int = higher_index * 2 + - 2
        ds: int = d + 1 # O número de diagonais em uma direção.
        # Rainhas em cada diagonal esquerda.
        r_diagonal_qs: list[int] = [0] * ds
        # Rainhas em cada diagonal direita.
        l_diagonal_qs: list[int] = [0] * ds

        # Calcula o fitness do seguinte modo:
        # [[x] [ ] [ ] [ ] [x]] r0: + 0 + 1 = 1
        # [[ ] [x] [ ] [ ] [ ]] r1: + 0
        # [[ ] [ ] [x] [x] [x]] r2: + 0 + 1 + 2 = 3
        # [[ ] [ ] [ ] [ ] [ ]]
        # [[ ] [ ] [ ] [ ] [ ]]
        # /e0: + 0 + 1 = 1     \d0: + 0 + 1 + 2 = 3
        # r: row, d: diagonal direita, e: diagonal esquerda
        # A cada casa marcada adiciona-se x onde x é o número de casas marcadas anteriormente.
        # Fitness será o total de rs + es + ds
        for col, row in enumerate(self.dna):
            row -= 1
            # Pares por coluna
            row_queens[row] += 1 # Conta mais uma rainha naquela linha.

            # A cada nova peça igual encontrada, incrementa o número anterior
            # de peças naquela coluna (incremento no número de pares formados na coluna).
            if row_queens[row] > 1:
                clashes += row_queens[row] - 1


            # Pares por diagonal (direita)
            rd: int = col - row # Índice da diagonal direita

            # A cada nova peça igual encontrada, incrementa o número anterior de peças
            # naquela diagonal (incremento no número de pares formados na diagonal direita).
            if rd < 0:
                if rd > -higher_index:
                    # Está numa diagonal direita: de d(n-1) à d([n-1] * 2 - 2)
                    rd += ds
                    r_diagonal_qs[rd] += 1

                    if r_diagonal_qs[rd] > 1:
                        clashes += r_diagonal_qs[rd] - 1

            elif rd < higher_index:
                # Está numa diagonal direita: de d0 à d([n-1]-1).
                r_diagonal_qs[rd] += 1

                if r_diagonal_qs[rd] > 1:
                    clashes += r_diagonal_qs[rd] - 1


            # Pares por diagonal (esquerda)
            ld: int = (higher_index - col) - row # Índice da diagonal esquerda

            # A cada nova peça igual encontrada, incrementa o número anterior de peças
            # naquela diagonal (incremento no número de pares formados na diagonal esquerda).
            if ld < 0:
                if ld > -higher_index:
                    # Está numa diagonal esquerda: de e(n-1) à e([n-1] * 2 - 2)
                    ld += ds
                    l_diagonal_qs[ld] += 1

                    if l_diagonal_qs[ld] > 1:
                        clashes += l_diagonal_qs[ld] - 1

            elif ld < higher_index:
                # Está numa diagonal esquerda: de d0 à e([n-1]-1).
                l_diagonal_qs[ld] += 1

                if l_diagonal_qs[ld] > 1:
                    clashes += l_diagonal_qs[ld] - 1

        # return clashes # Minimização
        return max_clashes - clashes # Maximização

    def get_fitness(self) -> int:
        '''Retorna a quantidade de pares de rainhas que não estão se atacando.'''
        return self._fitness

    def get_row(self, from_col: int) -> int:
        '''Dado uma rainha na coluna indicada, retorna o índice da linha em que está posicionada.'''
        return self.dna[from_col] - 1

    def __str__(self) -> str:
        # return f'id:{self.id}, gen:{self.generation}, fit:{self.get_fitness()}'
        return f'id:{self.id}, fit:{self.get_fitness()}'

    def __repr__(self) -> str:
        return f'{self.dna}: {self.get_fitness()}'

    def __init__(self, dna: list[int], generation: int = 0) -> None:
        self.dna = tuple(dna)
        self.id = next_id()
        self.generation = generation
        self._fitness = self._get_fitness()


class IndividualFactory():
    '''
    Define uma "interface" para geração de indivíduos.

    * Nota: Como o Python usa tipagem-pato, não é necessário "implementar" essa classe.
    Portanto, a mesma serve apenas como um rótulo para type-hints.
    '''
    def create() -> Individual:
        pass


class RandomIndividualFactory():
    '''
    Gera indivíduos aleatoriamente.
    '''

    @staticmethod
    def create() -> Individual:
        dna = [0] * 8

        for row in range(TABLE_SIZE):
            dna[row] = randint(1, TABLE_SIZE)

        return Individual(dna)


class BaseIndividualFactory():
    '''
    Gera indivíduos com base em valores pré-determinados.
    '''
    next_dna: int = 0
    dnas: list[list[int]] = [
        [1, 1, 1, 1, 1, 1, 1, 1], # coluna 0
        [8, 8, 8, 8, 8, 8, 8, 8], # coluna 7
        [1, 2, 3, 4, 5, 6, 7, 8], # diagonal direita: d0
        [8, 7, 6, 5, 4, 3, 2, 1], # diagonal esquerda: e0

        #[8, 1, 2, 3, 4, 5, 6, 7], # diagonal direita: d1
        #[7, 6, 5, 4, 3, 2, 1, 8], # diagonal esquerda: e1

        [2, 3, 4, 5, 6, 7, 8, 1], # diagonal direita: d12
        [1, 8, 7, 6, 5, 4, 3, 2], # diagonal esquerda: d12

        [5, 6, 7, 4, 5, 6, 7, 6],
        [8, 3, 7, 4, 2, 5, 1, 6],

        # [7, 8, 6, 5, 4, 3, 1, 2],
        # [2, 1, 3, 4, 5, 6, 8, 7],
    ]
    target_fitness: list[int] = [
        0, 0, 0, 0,
        #22, 22,
        22, 22, #
                0,
        17, 1
    ]

    def create(self) -> Individual:
        '''Retorna um indivíduo com o próximo dna-base pré-determinado.'''
        dna: list[int] = self.dnas[self.next_dna]
        self.next_dna += 1
        self.next_dna %= len(self.dnas)

        return Individual(dna)
