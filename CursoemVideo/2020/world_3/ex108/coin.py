def increase(n: float = 0, value: float = 1) -> float:
    return n + n * value


def decrease(n: float = 0, value: float = 1) -> float:
    return n - n * value


def double(n: float = 0) -> float:
    return n * 2


def half(n: float = 0) -> float:
    return n / 2


def coin(value: float = 0, sign: str = 'R$') -> str:
    return f'{sign}{value:.2f}'.replace('.', ',')
