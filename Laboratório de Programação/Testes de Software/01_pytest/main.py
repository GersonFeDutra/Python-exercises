from typing import Union
_NUMBER = Union[int, float]


def func(x: _NUMBER) -> _NUMBER:
    return x + 1


def test_answer() -> None:
    # assert func(3) == 5
    assert func(3) == 4
