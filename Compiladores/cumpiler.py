#!./venv/bin/python3
"""Usage: python ./cumpyler.py <source_file> [-l|--lexer]
    @option [-l|--lexer] stop on lexer
"""

from enum import Enum
import sys


EXIT_ERROR: int = 1

if __name__ == "__main__":
    class StopOn(Enum):
        NONE = 0
        LEXER = 1

    #region Options
    stop: StopOn = StopOn.NONE
    optimize = True  # Allows to use an accumulator to process result directly
    #enderegion

    #region 1. Verifica se o usuário passou o nome do arquivo
    if len(sys.argv) < 2:
        print('\033[33m', end='')
        print(f'Usage: python {sys.argv[0]} <source_file> [-no|--no-optimize] [-l|--lexer]')
        print('\t' '[-l|--lexer] stop on lexer. log output')
        print('\t' "[-no|--no-optimize] don't use accumulator")
        print('\033[m', end='')
        sys.exit(EXIT_ERROR)
    #endregion
    #region 2. Verifica se foram passadas opções
    elif len(sys.argv) > 2:
        for i in range(2, len(sys.argv)):
            if sys.argv[i] in ['-l', '--lexer']:
                stop = StopOn.LEXER
    #endregion

    from lexer import Lexer
    source_filename = sys.argv[1]

    match stop:
        case StopOn.LEXER:
            #region 3. Processa o arquivo usando o analisador léxico
            #source_filename = "code.las"
            lexer = Lexer(source_filename)
            lexer.start()
            #endregion
        case _:
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
                print(f"Erro: O arquivo '{source_filename}' não foi encontrado.")
            except ParseError:
                print("\nErro de Sintaxe")
