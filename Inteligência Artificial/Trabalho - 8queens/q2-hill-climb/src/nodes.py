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

class Node():
    '''
    Um indivíduo de uma população.
    Representa uma rainha no problema das 8 rainhas.

    @properties
        state:
            Cada posição na tupla `state` representará a coluna que a rainha será posicionada.
            Enquanto que o valor dado naquela posição indica a linha.
        generation:
            Em que geração esse indivíduo foi gerado.
        id:
            Identificador único do indivíduo.

    @methods
        get_fitness():
            O valor de adaptação do indivíduo.
    '''
    state: tuple[int] # Definido como tupla, pois o dna deve ser fixo para cada indivíduo.
    successor_n: int
    id: int

    def show(self) -> None:
        print(f'{self}')

        for row in range(TABLE_SIZE):
            self.show_row(row)
            print()

        print(f'sucessor n°:{self.successor_n}')
        print(f'state:{self.state}')

    def show_row(self, row) -> None:

        for col in range(TABLE_SIZE):
            print(f'{("👑" if self.get_row(col) == row else ( "⬛" if (row + (col % 2)) % 2 == 0 else "⬜")):^1s}', end='')

    def _h(self) -> int:
        '''
        Calcula a heurística de um nó no problema das 8 rainhas em `O(n)`,
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

        # Calcula a heurística do seguinte modo:
        # [[x] [ ] [ ] [ ] [x]] r0: + 0 + 1 = 1
        # [[ ] [x] [ ] [ ] [ ]] r1: + 0
        # [[ ] [ ] [x] [x] [x]] r2: + 0 + 1 + 2 = 3
        # [[ ] [ ] [ ] [ ] [ ]]
        # [[ ] [ ] [ ] [ ] [ ]]
        # /e0: + 0 + 1 = 1     \d0: + 0 + 1 + 2 = 3
        # r: row, d: diagonal direita, e: diagonal esquerda
        # A cada casa marcada adiciona-se x onde x é o número de casas marcadas anteriormente.
        # A heurística será o total de rs + es + ds
        for col, row in enumerate(self.state):
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

        # return max_clashes - clashes # Maximização
        return clashes # Minimização

    def h(self) -> int:
        '''Heurística: Retorna a quantidade de pares de rainhas que estão se atacando.'''
        return self._heuristic

    def get_successor(self):
        '''
        Retorna um nó sucessor com a melhor heurística:
        Os sucessores de um estado são todos os estados possíveis gerados pela
        movimentação de uma única rainha para outro quadrado da mesma coluna.
        Se nenhum estado tiver uma heurística melhor que a do nó atual, retorna ele mesmo.
        '''
        lowest: Node = self

        for row in range(TABLE_SIZE):
            for col in range(TABLE_SIZE):
                if row == self.get_row(col):
                    continue
                new = list(self.state)
                new[col] = row + 1 # Linhas são contadas à partir do 1.
                successor = Node(new, self.successor_n + 1)

                if successor.h() < lowest.h():
                    lowest = successor

        return lowest

    def get_row(self, from_col: int) -> int:
        '''Dado uma rainha na coluna indicada, retorna o índice da linha em que está posicionada.'''
        return self.state[from_col] - 1

    def __str__(self) -> str:
        # return f'id:{self.id}, gen:{self.generation}, fit:{self.get_fitness()}'
        return f'id:{self.id}, fit:{self.h()}'

    def __repr__(self) -> str:
        return f'{self.state}: {self.h()}'

    def __init__(self, initial_state: list[int], generation: int = 0) -> None:
        self.state = tuple(initial_state)
        self.id = next_id()
        self.successor_n = generation
        self._heuristic = self._h()


class NodeFactory():
    '''
    Define uma "interface" para geração de indivíduos.

    * Nota: Como o Python usa tipagem-pato, não é necessário "implementar" essa classe.
    Portanto, a mesma serve apenas como um rótulo para type-hints.
    '''
    def create_node() -> Node:
        pass


class RandomNodeFactory():
    '''
    Gera indivíduos aleatoriamente.
    '''

    @staticmethod
    def create_node() -> Node:
        dna = [0] * 8

        for row in range(TABLE_SIZE):
            dna[row] = randint(1, TABLE_SIZE)

        return Node(dna)


class BaseNodeFactory():
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

    def create_node(self) -> Node:
        '''Retorna um indivíduo com o próximo dna-base pré-determinado.'''
        dna: list[int] = self.dnas[self.next_dna]
        self.next_dna += 1
        self.next_dna %= len(self.dnas)

        return Node(dna)
