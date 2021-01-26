price: float = float(input('What is the price of your house? R$ '))
salary: float = float(input('What is your salary? R$ '))
years: int = int(input('How many years do you wanna to pay? '))
installment: float = price / years / 12  # or -> price / (years * 12)
salary_limit: float = salary * 30 / 100

if installment <= salary_limit:
    print(f"The monthly installment is gonna cost you\033[32m R${installment:.2f} by month.\033[m")

else:
    print(
        f'\033[31mThe loan was denied.\033[m The monthly payment (R${installment:.2f}) can\'t be higher than'
        f'\033[33m R${salary_limit:.2f} (30% of your salary).\033[m'
    )
