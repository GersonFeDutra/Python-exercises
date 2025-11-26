from enum import IntEnum
import sys


class TAG(IntEnum):
    NUM = 256
    ID = 257
    TRUE = 258 # apenas para ilustrar
    FALSE = 259 # apenas para ilustrar


class Lexer:
    def __init__(self, filename: str):
        self._line = 1
        self._peek = ' '
        self._pos = 0
        self._id_table = {}
        self._open_source_file(filename)

    def _open_source_file(self, filename: str):
        
        try:
            with open(filename, 'r') as file:
                self._source_code = file.read()
                
                # (Opcional) Remove espaços em branco extras no final do arquivo 
                # para evitar erros com editores que salvam muitas linhas vazias
                self._source_code = self._source_code.strip()
        except FileNotFoundError:
            print(f"Erro: O arquivo '{filename}' não foi encontrado.")

    def _init_id_table(self):
        self._id_table = {
            "true": Token(TAG.TRUE),
            "false": Token(TAG.FALSE)
        }

    def _get_next_char(self):
        """Simual o cin.get() lendo da string armazenada"""
        # Implementação do método para obter o próximo caractere do código fonte
        while self._pos < len(self._source_code):
            char = self._source_code[self._pos]
            # Se for espaço ou tabulação, ignora
            self._pos += 1
            if char in ['\t']: 
                continue
            return char
        return '' # Fim da entrada

    def _scan(self):
        # Implementação do método de varredura (scan) do lexer
        while self._peek.isspace():
            if self._peek == '\n':
                self._line += 1
                print()
                print(f"Linha {self._line}: ", end='', flush=True)
            self._peek = self._get_next_char() 
            
        # Trata números inteiros
        if self._peek.isdigit():
            num_str = ""
            while self._peek.isdigit():
                num_str += self._peek
                self._peek = self._get_next_char()
                
            num = int(num_str)
            print(f"<NUM, {num}> ", end='', flush=True)
            return Num(num)
        
        # Trata identificadores e palavras reservadas
        if self._peek.isalpha():
            id_str = ""
            while self._peek.isalpha():
                id_str += self._peek
                self._peek = self._get_next_char()
                
            if id_str in self._id_table:
                # para debugging
                token_found = self._id_table[id_str]
                
                if token_found.tag == TAG.TRUE:
                    print(f"<TRUE> ", end='', flush=True)
                elif token_found.tag == TAG.FALSE:
                    print(f"<FALSE> ", end='', flush=True)
                
                print(f"<ID, {token_found.name}> ", end='', flush=True)     
                return self._id_table[id_str]
            
            # se o identificador não estiver na tabela, cria um novo
            else:
                new_id = Id(id_str)
                self._id_table[id_str] = new_id
                print(f"<ID, {new_id.name}> ", end='', flush=True)
                return new_id
            
        # Trata operadores
        t_oper = Token(self._peek)
        print(f"<'{t_oper.tag}'> ", end='', flush=True)
        self._peek = self._get_next_char()
        
        return t_oper

    def start(self):
        print("Linha 1: ", end='', flush=True)
        while (self._peek != ''):
            self._scan()


class Token:
    def __init__(self, tag: TAG):
        self.tag = tag


class Id(Token):
    def __init__(self, name: str):
        super().__init__(TAG.ID)
        self.name = name


class Num(Token):
    def __init__(self, value: int):
        super().__init__(TAG.NUM)
        self.value = value
