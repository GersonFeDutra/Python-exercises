def square(x):
    """square a number"""
    return x ** 2


if __name__ == "__main__":
    print("This is a module")

for N in range(1, 4):
    print(f"{N} squared is {square(N)}")
