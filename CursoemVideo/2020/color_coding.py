DEF: str = '\033['


class Style:
    NONE: str = '\033[0m'
    I: str = '\033[1m'
    B: str = '\033[2m'
    U: str = '\033[4m'
    INVERSE: str = '\033[7m'


class Color:
    WHITE: str = '\033[30m'
    RED: str = '\033[31m'
    GREEN: str = '\033[32m'
    YELLOW: str = '\033[33m'
    BLUE: str = '\033[34m'
    MAGENTA: str = '\033[35m'
    CYAN: str = '\033[36m'
    GRAY: str = '\033[37m'


class Back:
    WHITE: str = '\033[40m'
    RED: str = '\033[41m'
    GREEN: str = '\033[42m'
    YELLOW: str = '\033[43m'
    BLUE: str = '\033[44m'
    MAGENTA: str = '\033[45m'
    CYAN: str = '\033[46m'
    GRAY: str = '\033[47m'
