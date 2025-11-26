#!./venv/bin/python3
"""Usage: python ./cumpyler.py <source_file> [-l|--lexer]
    @option [-?|--help] show help
    @option [-!|--log] log intermediary output
    @option [-l|--lexer] options on lexer. Enable log
    @option [-no|--no-optimize] don't use accumulator
"""

from enum import Enum
import sys


EXIT_ERROR: int = 1

def show_help() -> None:
    print('\033[34m'
        f'Usage: python {sys.argv[0]} <source_file> [-!|--log] [-no|--no-optimize] [-l|--lexer]\n'
        '\t[-?|--help] show this help\n'
        '\t[-!|--log] log intermediary output\n'
        '\t[-l|--lexer] options on lexer. Enable log\n'
        "\t[-no|--no-optimize] don't use accumulator\n"
        '\033[m')


def err(message: str, *args, **kwargs):
    # Note that stderr is unbuffered: always flush.
    print(f'\033[31m{message}\033[m', *args, file=sys.stderr, **kwargs)


if __name__ == "__main__":
    class Options(Enum):
        NONE = 0
        LEXER = 1
        LOG = 2

    #region Options
    options: Options = Options.NONE
    optimize = True  # Allows to use an accumulator to process result directly
    #endregion

    #region 1. Verifica se o usuário passou o nome do arquivo
    if len(sys.argv) < 2:
        print('\033[31m' 'Error: No file name provided' '\033[m', file=sys.stderr)
        show_help()
        sys.exit(EXIT_ERROR)
    #endregion
    #region 2. Verifica se foram passadas opções
    elif len(sys.argv) > 2:
        for i in range(2, len(sys.argv)):
            if sys.argv[i] in ['-?', '--help']:
                show_help()
                sys.exit()
            if sys.argv[i] in ['-l', '--lexer']:
                options |= Options.LEXER
                options |= Options.LOG
            if sys.argv[i] in ['-!', '--log']:
                options |= Options.LOG
            if sys.argv[i] in ['-no', '--no-optimize']:
                optimize = False
    #endregion

    from lexer import Lexer
    source_filename = sys.argv[1]

    if options & Options.LEXER:
        #region 3. Processa o arquivo usando o analisador léxico
        #source_filename = "code.las"
        lexer = Lexer(source_filename, log_enabled=True)
        lexer.start()
        #endregion
    else:
        # Equivalente ao main() do postfix.cpp
        from parser import Parser, ParseError

        try:
            #region 3. Abre o arquivo e lê todo o conteúdo
            with open(source_filename, 'r') as file:
                content = file.read()

                # (Opcional) Remove espaços em branco extras no final do arquivo 
                # para evitar erros com editores que salvam muitas linhas vazias
                content = content.strip()
            #endregion

            #region 4. Inicia o Parser com o conteúdo do arquivo
            tradutor = Parser(content, optimize)
            tradutor.start()
            #endregion

            print() # quebra de linha final
        except FileNotFoundError:
            err(f"Erro: O arquivo '{source_filename}' não foi encontrado.")
        except ParseError:
            err("\nErro de Sintaxe")
