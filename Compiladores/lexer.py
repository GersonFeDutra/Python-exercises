from enum import IntEnum
import sys


class TAG(IntEnum):
    ...
    NUM = 256
    ID = 257
    TRUE = 258 # apenas para ilustrar
    FALSE = 259 # apenas para ilustrar


def log(*args, **kwargs):
    # Note that stderr is unbuffered: always flush.
    print(*args, file=sys.stderr, **kwargs)


class Lexer:
    def __init__(self, filename: str, log_enabled: bool = False):
        self._line = 1
        self._peek = ' '
        self._pos = 0
        self._id_table = {}
        self._open_source_file(filename)
        if log_enabled:
            self._log = log
        else:
            self._log = lambda *args, **kwargs: None

    def _open_source_file(self, filename: str):
        """
        Abre o arquivo de código fonte e carrega seu conteúdo na variável
        _source_code.

        :param filename: nome do arquivo a ser aberto
        """
        with open(filename, 'r') as file:
            self._source_code = file.read()
            
            # (Opcional) Remove espaços em branco extras no final do arquivo
            # para evitar erros com editores que salvam muitas linhas vazias
            self._source_code = self._source_code.strip()

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

    def scan(self):
        """Implementação do método de varredura (scan) do lexer."""
        #region 1. Conta o número de linhas, ignorando os espaços em branco
        while self._peek.isspace():
            if self._peek == '\n':
                self._line += 1
                self._log()
                self._log(f"Linha {self._line}: ", end='')
            self._peek = self._get_next_char() 
        #endregion

        #region 2. Ignora comentários [ #...\n and /*...*/ ]
        if self._peek == '#':
            while self._peek != '\n' and self._peek != '':
                self._peek = self._get_next_char()
        if self._peek == '/' and len(self._source_code) > self._pos and self._source_code[self._pos] == '*':
            while self._peek != '*' or len(self._source_code) <= self._pos or \
                  self._source_code[self._pos] != '/':
                self._peek = self._get_next_char()
            self._get_next_char()
            self._peek = self._get_next_char()
        #endregion

        #region 2. Trata números inteiros
        if self._peek.isdigit():
            num_str = ""
            while self._peek.isdigit():
                num_str += self._peek
                self._peek = self._get_next_char()
                
            num = int(num_str)
            self._log(f"<NUM, {num}> ", end='')
            return Num(num)
        #endregion

        #region 3. Trata identificadores e palavras reservadas
        if self._peek.isalpha():
            id_str = ""
            while self._peek.isalpha():
                id_str += self._peek
                self._peek = self._get_next_char()
            
            if id_str in self._id_table:
                # para debugging
                token_found = self._id_table[id_str]
                
                if token_found.tag == TAG.TRUE:
                    self._log(f"<TRUE> ", end='')
                elif token_found.tag == TAG.FALSE:
                    self._log(f"<FALSE> ", end='')
                
                self._log(f"<ID, {token_found.name}> ", end='')     
                return self._id_table[id_str]
            
            # se o identificador não estiver na tabela, cria um novo
            else:
                new_id = Id(id_str)
                self._id_table[id_str] = new_id
                self._log(f"<ID, {new_id.name}> ", end='')
                return new_id
        #endregion

        #region 4. Trata operadores
        t_oper = Token(self._peek)
        self._log(f"<'{t_oper.tag}'> ", end='')
        self._peek = self._get_next_char()
        #endregion

        return t_oper

    def start(self):
        self._log("Linha 1: ", end='')
        while (self._peek != ''):
            self.scan()
        self._log()


class Token:
    def __init__(self, tag: TAG):
        self.tag = tag

    def __eq__(self, value: TAG | str) -> bool:
        return value is TAG and self.tag == value \
            or value is str and self.tag == TAG.ID

    def __ne__(self, value: TAG | str) -> bool:
        return value is TAG and self.tag != value \
            or value is str and self.tag != TAG.ID


class Id(Token):
    def __init__(self, name: str):
        super().__init__(TAG.ID)
        self.name = name


class Num(Token):
    def __init__(self, value: int):
        super().__init__(TAG.NUM)
        self.value = value
