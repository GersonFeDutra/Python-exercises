majors: int = 0
males: int = 0
females_under_twenties: int = 0


def get_input_option(message: str, options: list) -> str:
    option: str = ""

    while not(option in options):
        option = input(message).lower()

    return option


while True:
    print(f"{'_' * 20}\nRegister a person: ")
    age: int = int(input("Enter a age: "))
    gender: str = get_input_option("Enter a gender: (m/f) ", ["m", "f"])

    if age >= 18:
        majors += 1

    if gender == "m":
        males += 1
    elif gender == "f" and age < 20:
        females_under_twenties += 1

    if get_input_option("Do you want to continue? (y/n) ", ["y", "n"]) == "n":
        break

print()
print(majors, "registered people are over 18 years old.")
print(males, "registered males were entered.")
print(females_under_twenties, "registered females have less than 20 years old.")
