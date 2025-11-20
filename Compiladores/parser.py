import sys

# Definimos uma exceção personalizada para evitar confusão 
# com o "SyntaxError" nativo do Python
class ParseError(Exception):
    pass

class Parser:
    def __init__(self, text: str, optimize=True):
        self.source = text + '\n'
        self.pos = 0
        self.lookahead = ''
        self.optimize = optimize
        if optimize:
            self.accumulator = 0

    def get_next_char(self):
        """Simula o cin.get() lendo da string armazenada"""
        while self.pos < len(self.source):
            char = self.source[self.pos]
            self.pos += 1
            # Se for espaço, tabulação ou quebra de linha (exceto a última), ignora
            if char in [' ', '\t', '\r']: 
                continue
            return char
        return ''  # Fim da entrada

    def start(self):
        """Inicia o processo de análise lendo o primeiro caractere."""
        # Lê 1 caractere da entrada padrão (equivalente ao cin.get())
        self.lookahead = self.get_next_char()
        self.expr()
        
        # Verifica se o último caractere é uma quebra de linha
        if self.lookahead != '\n':
            raise ParseError()

    def expr(self):
        """
        Regra: expr -> digit* oper
        Aceita números maiores que 9 (mais de um dígito)
        """
        self.accumulator = self.digit()
        if self.optimize:
            while True:
                # Regra: oper -> + digit { print(+) } oper
                if self.lookahead == '+':
                    self.match('+')
                    self.accumulator += self.digit()
                # Regra: oper -> - digit { print(-) } oper
                elif self.lookahead == '-':
                    self.match('-')
                    self.accumulator -= self.digit()
                # Produção vazia (return)
                else:
                    print(self.accumulator)
                    return
        else:
            while True:
                # Regra: oper -> + digit { print(+) } oper
                if self.lookahead == '+':
                    self.match('+')
                    print(' ', end='', flush=True)
                    self.digit()
                    print('+', end='', flush=True)
                
                # Regra: oper -> - digit { print(-) } oper
                elif self.lookahead == '-':
                    self.match('-')
                    print(' ', end='', flush=True)
                    self.digit()
                    print('-', end='', flush=True)
                
                # Produção vazia (return)
                else:
                    return

    def digit(self) -> int:
        """
        Regra: digit -> digit { print(digit) }
        """
        value = 0
        if self.optimize:
            while self.lookahead.isdigit():
                try:
                    value *= 10
                    value += int(self.lookahead)
                    self.match(self.lookahead)
                except ParseError:
                    return 0
        else:
            while self.lookahead.isdigit():
                try:
                    print(self.lookahead, end='', flush=True)
                    self.match(self.lookahead)
                except ParseError:
                    return 0

        return value

    def match(self, t):
        """Verifica se o caractere atual corresponde ao esperado e avança."""
        if t == self.lookahead:
            self.lookahead = self.get_next_char()
        else:
            raise ParseError()

# Equivalente ao main() do postfix.cpp
if __name__ == "__main__":
    # 1. Verifica se o usuário passou o nome do arquivo
    if len(sys.argv) < 2:
        print("Uso: python parser.py <arquivo_fonte> [-no|--no-optimize]")
        sys.exit(1)

    nome_arquivo = sys.argv[1]

    optimize = True  # Allows to use an accumulator to process result directly
    if len(sys.argv) > 2:
        optimize = not(sys.argv[2] == '-no' or sys.argv[2] == '--no-optimize')

    try:
        # 2. Abre o arquivo e lê todo o conteúdo
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()

            # (Opcional) Remove espaços em branco extras no final do arquivo 
            # para evitar erros com editores que salvam muitas linhas vazias
            conteudo = conteudo.strip()

        # 3. Inicia o Parser com o conteúdo do arquivo
        tradutor = Parser(conteudo, optimize)
        tradutor.start()

        print() # quebra de linha final
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except ParseError:
        print("\nErro de Sintaxe")
