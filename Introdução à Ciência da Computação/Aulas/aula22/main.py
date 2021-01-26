import utils_module # Import your script as a module in the main script. It runs when imported.
from utils_package import numbers # Import the package numbers inside the package utils_package.

print(numbers.factorial(5))
print(' =', numbers.factorial(5, True))
result: int = numbers.factorial(10, True)
print()
print(f'{result:>38}')
help(numbers.factorial)
print(numbers.doble(2))
print(numbers.triple(3))
