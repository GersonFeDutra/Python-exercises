from datetime import date

year = int(input('What year we are now? (Enter 0 to the current year): '))
# is_leap_year: bool = True if (year % 400 == 0) else (year % 4 == 0 and year % 100 != 0)

if year == 0:
    year = date.today().year

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  # Optimized
    print(f'{year} is a leap year!')
else:
    print(f'{year} is not a leap year!')
