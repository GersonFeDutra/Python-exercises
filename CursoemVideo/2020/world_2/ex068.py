from random import randint


def get_option() -> int:
    option: int = -1

    while option != 0 or option != 1:
        option = int(input("Even (0) or odd (1)? "))

    return option


while True:
    print("_" * 20)
    is_option_odd: int = get_option()
    number: int = int(input("Enter a integer: "))
    random_number: int = randint(0, 10)
    result: int = number + random_number
    rest: int = result % 2

    print(f"I choose {random_number}!")
    print(f"{number} + {random_number} = {result}")
    print(f"{result} is {'even' if rest == 0 else 'odd'}.", end=" ")

    if (rest - is_option_odd) == 0:
        print("\033[32mYou win!\033[m")
    else:
        print("\033[31mYou lose!\033[m")
        break
