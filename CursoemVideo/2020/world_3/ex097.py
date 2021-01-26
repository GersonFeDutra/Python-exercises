def write(message: str) -> None:
    width: int = len(message) + 4
    line: str = '-' * width

    print(line)
    print(message.center(width))
    print(line)


write('Hello World!')
print()
write('Have a nice day!')
