def input_coin(message: str) -> float:
    entry: str

    while True:
        entry = input(message).strip().replace(',', '.', 1)

        if entry.replace(',', '.', 1).replace('.', '', 1).isdigit():
            break

    return float(entry)
