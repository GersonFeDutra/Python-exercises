def increase(n: float = 0, value: float = 1, as_coin: bool = False):
    result: float = n + n * value

    return to_coin(result) if as_coin else result


def decrease(n: float = 0, value: float = 1, as_coin: bool = False) -> float:
    result: float = n - n * value

    return to_coin(result) if as_coin else result


def double(n: float = 0, as_coin: bool = False):
    result: float = n * 2

    return to_coin(result) if as_coin else result


def half(n: float = 0, as_coin: float = False):
    result: float = n / 2

    return to_coin(result) if as_coin else result


def to_coin(value: float = 0, sign: str = 'R$') -> str:
    return f'{sign}{value:.2f}'.replace('.', ',')
