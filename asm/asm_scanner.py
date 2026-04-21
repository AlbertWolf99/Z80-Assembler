from asm.asm_token import Token, TokenType

class AsmScanner:
    def __init__(self, filename: str):
        self.__input_file = open(filename, 'r')
        self.__filename = filename
        self.__line = 0
        self.__col = 0
        self.__src_code = ""
        self.__content = ""
        self.next_line()
    
    def scan(self) -> Token:
        self.__content = ""
        while self._is_same_char(" ") or self._is_same_char("\t") or self._is_same_char("\n"):
            self._next_char()
        cur_col = self.__col
        if self._cur_char() == "\0" or self._cur_char() == ";":
            return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.EOL)
        if self._is_digit():
            while self._is_digit():
                self._append()
                self._next_char()
            return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.INTEGER_LITERAL, int(self.__content))
        if self._cur_char() == "$":
            self._next_char()
            if self._is_hex():
                while self._is_hex():
                    self._append()
                    self._next_char()
                return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.INTEGER_LITERAL, int(self.__content, 16))
            if self._cur_char == "$":
                self._next_char()
                return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.START_POSITION)
            return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.CURRENT_POSITION)
        if self._is_symbol():
            while self._is_symbol():
                self._append_lower()
                self._next_char()
            return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.SYMBOL)
        if self._cur_char() == "(":
            self._next_char()
            return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.LEFT_PARENTHESIS)
        if self._cur_char() == ")":
            self._next_char()
            return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.RIGHT_PARENTHESIS)
        if self._cur_char() == "-":
            self._next_char()
            return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.MINUS)
        if self._cur_char() == "+":
            self._next_char()
            return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.PLUS)
        if self._cur_char() == "%":
            self._next_char()
            return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.MODULO)
        if self._cur_char() == "/":
            self._next_char()
            return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.DIVISION)
        if self._cur_char() == ",":
            self._next_char()
            return Token(self.__filename, self.__line, cur_col, self.__content, TokenType.COMMA)
        raise Exception(f"Error: {self.__filename}:{self.__line}:{self.__col}: Unknown character")
    
    def next_line(self):
        self.__src_code = self.__input_file.readline()
        self.__line += 1
        self.__col = 0
    
    def is_eof(self) -> bool:
        return self.__src_code == "" and self._cur_char() == "\0"
    
    def _append(self):
        self.__content += self._cur_char()
    
    def _append_lower(self):
        self.__content += self._cur_char().lower()
    
    def _next_char(self):
        self.__col += 1
    
    def _cur_char(self) -> str:
        return self.__src_code[self.__col] if self.__col < len(self.__src_code) else "\0"

    def _is_same_char(self, c: str) -> bool:
        return self._cur_char() == c
    
    def _is_digit(self) -> bool:
        return self._cur_char().isdigit()
    
    def _is_symbol(self) -> bool:
        return self._cur_char().isdigit() or self._cur_char().isalpha() or self._cur_char() == "_" or self._cur_char() == "."
    
    def _is_hex(self) -> bool:
        return self._is_digit() or 'A' <= self._cur_char() <= 'F' or 'a' <= self._cur_char() <= 'f'
