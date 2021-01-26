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


def resume(price: float, percent_on: float = 0, percent_off: float = 0) -> None:
    print(f'Half: {half(price, True)}.')
    print(f'Double: {double(price, True)}.')
    print(f'Increased by {percent_on}%: {increase(price, percent_on / 100, True)}.')
    print(f'Decreased by {percent_off}%: {decrease(price, percent_off / 100, True)}.')
