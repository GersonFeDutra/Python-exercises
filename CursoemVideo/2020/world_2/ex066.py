length: int = 0
numbers_sum: float = 0

while True:
    # The exercise "flag" was changed from 999 to 0. Out of personal preference.
    number: float = float(input("Enter a number (press 0 to stop): "))

    if number == 0:
        break

    length += 1
    numbers_sum += number

print(f"You entered {length}, and the sum between them is {numbers_sum}.")
