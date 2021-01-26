total: float = 0
over_a_thousand: float = 0
cheaper_price: float = -1
cheaper_name: str = ""


def can_continue() -> bool:
    answer: str = ""

    while answer != "y" and answer != "n":
        answer = input("Do you want to continue? (y/n) ").lower()

    return answer == "y"


while True:
    name: str = input("Enter a name of a product: ")
    price: float = float(input("Enter the price of this product: $"))
    total += price

    if price > 1000:
        over_a_thousand += 1

    if cheaper_price == -1 or price < cheaper_price:
        cheaper_price = price
        cheaper_name = name

    if not can_continue():
        break

print()
print(f"The total paid was ${total:.2f}.")
print(f"{over_a_thousand} products cost over a thousand dollars.")
print(f"{cheaper_name} is the cheaper product, costing ${cheaper_price}.")
