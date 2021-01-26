while True:
    number: int = int(input("Enter an integer to show his multiplication table (enter a negative number to exit): "))

    if number < 0:
        break

    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")

    print("_" * 12)
