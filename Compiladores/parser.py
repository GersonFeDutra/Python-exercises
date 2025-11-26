import sys

from lexer import Lexer, Token, TAG
from options import *


# Definimos uma exceção personalizada para evitar confusão 
# com o "SyntaxError" nativo do Python
class ParseError(Exception):
    pass

class Parser:

    def __init__(self, filename: str, opts: Options):
        self._lexer = Lexer(filename, opts & Options.LOG)
        self._lookahead = Token('')
        self._optimize = bool(opts & Options.OPTIMIZE)
        if self._optimize:
            self.accumulator: int = 0

    def start(self):
        """Inicia o processo de análise lendo o primeiro token."""
        self._lookahead = self._lexer.scan()
        self.expr()
        
        # Verifica se o último caractere é o marcador vazio (nil ⇒ EOF)
        if self._lookahead != '':
            raise ParseError()

    def expr(self):
        """
        Regra: expr -> digit* oper
        Aceita números maiores que 9 (mais de um dígito)
        """
        self.accumulator = self.digit()
        if self._optimize:
            while True:
                # Regra: oper -> + digit { print(+) } oper
                if self._lookahead == '+':
                    self.match('+')
                    self.accumulator += self.digit()
                # Regra: oper -> - digit { print(-) } oper
                elif self._lookahead == '-':
                    self.match('-')
                    self.accumulator -= self.digit()
                # Produção vazia (return)
                else:
                    print(self.accumulator)
                    return
        else:
            while True:
                # Regra: oper -> + digit { print(+) } oper
                if self._lookahead == '+':
                    self.match('+')
                    print(' ', end='', flush=True)
                    self.digit()
                    print('+', end='', flush=True)
                
                # Regra: oper -> - digit { print(-) } oper
                elif self._lookahead == '-':
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
        if self._lookahead.tag == TAG.NUM:
            print(self._lookahead.value, end='', flush=True)
            self.match(self._lookahead.tag)
            return self._lookahead.tag
        else:
            raise ParseError()

    def match(self, t: TAG):
        """Verifica se o caractere atual corresponde ao esperado e avança."""
        if t == self._lookahead.tag:
            self._lookahead = self._lexer.scan()
        else:
            raise ParseError()
