amount: int = int(input("What will be the amount drawn? (integer) "))
banknotes: dict = {
    50: 0,
    20: 0,
    10: 0,
    1: 0,
}


def drawn(value: int) -> None:
    global amount, banknotes

    while amount - value >= 0:
        banknotes[value] += 1
        amount -= value

        if amount == 0:
            break


for banknote in banknotes:
    drawn(banknote)

    if banknotes[banknote] != 0:
        print(f"Total of {banknotes[banknote]} notes of ${banknote:.2f}")
