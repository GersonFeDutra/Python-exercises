from typing import Union
from math import inf
_NUMBER = Union[int, float]


def test(_input: list[_NUMBER], _min: _NUMBER, _max: _NUMBER) -> None:
    sl = SmallestLargest(_input)
    assert sl.get_smallest() == _min
    assert sl.get_largest() == _max
    print('Test Passed!')


class SmallestLargest():

    def get_smallest(self) -> None:
        return self._smallest

    def get_largest(self) -> None:
        return self._largest
    
    def __init__(self, entries: list[_NUMBER]) -> None:
        self._largest = -inf
        self._smallest = inf
        
        for entry in entries:
            
            if entry < self._smallest:
                self._smallest = entry
            # elif entry > self._largest: # Erro detectado
            if entry > self._largest:
                self._largest = entry


if __name__ == '__main__':
    test([4, 25, 7, 9], 4, 25)
    test([4, 3, 2, 1], 1, 4)
