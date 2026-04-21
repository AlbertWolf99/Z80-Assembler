from asm.asm_token import Token, TokenType

class AsmScanner:
    def __init__(self, filename: str):
        self._input_file = open(filename, 'r')
        self._filename = filename
        self._line = 0
        self._col = 0
        self._src_code = ""
        self._content = ""
        self.next_line()
    
    def next_line(self):
        self._src_code = self._input_file.readline()
        self._line += 1
        self._col = 0
    
    def is_eof(self) -> bool:
        return self._src_code == "" and self._cur_char() == "\0"
    
    def get_current_token(self) -> Token:
        return self._token

    def get_next_token(self) -> Token:
        self._token = self._scan()
        return self._token
    

    def _scan(self) -> Token:
        self._content = ""
        while self._is_same_char(" ") or self._is_same_char("\t") or self._is_same_char("\n"):
            self._next_char()
        cur_col = self._col
        if self._cur_char() == "\0" or self._cur_char() == ";":
            return Token(self._filename, self._line, cur_col, self._content, TokenType.EOL)
        if self._is_digit():
            while self._is_digit():
                self._append()
                self._next_char()
            return Token(self._filename, self._line, cur_col, self._content, TokenType.INTEGER_LITERAL, int(self._content))
        if self._cur_char() == "$":
            self._next_char()
            if self._is_hex():
                while self._is_hex():
                    self._append()
                    self._next_char()
                return Token(self._filename, self._line, cur_col, self._content, TokenType.INTEGER_LITERAL, int(self._content, 16))
            if self._cur_char == "$":
                self._next_char()
                return Token(self._filename, self._line, cur_col, self._content, TokenType.START_POSITION)
            return Token(self._filename, self._line, cur_col, self._content, TokenType.CURRENT_POSITION)
        if self._is_symbol():
            while self._is_symbol():
                self._append_lower()
                self._next_char()
            return Token(self._filename, self._line, cur_col, self._content, TokenType.SYMBOL)
        if self._cur_char() == "(":
            self._next_char()
            return Token(self._filename, self._line, cur_col, self._content, TokenType.LEFT_PARENTHESIS)
        if self._cur_char() == ")":
            self._next_char()
            return Token(self._filename, self._line, cur_col, self._content, TokenType.RIGHT_PARENTHESIS)
        if self._cur_char() == "-":
            self._next_char()
            return Token(self._filename, self._line, cur_col, self._content, TokenType.MINUS)
        if self._cur_char() == "+":
            self._next_char()
            return Token(self._filename, self._line, cur_col, self._content, TokenType.PLUS)
        if self._cur_char() == "%":
            self._next_char()
            return Token(self._filename, self._line, cur_col, self._content, TokenType.MODULO)
        if self._cur_char() == "/":
            self._next_char()
            return Token(self._filename, self._line, cur_col, self._content, TokenType.DIVISION)
        if self._cur_char() == ",":
            self._next_char()
            return Token(self._filename, self._line, cur_col, self._content, TokenType.COMMA)
        if self._cur_char() == "[":
            self._next_char()
            return Token(self._filename, self._line, cur_col, self._content, TokenType.LEFT_INDEX)
        if self._cur_char() == "]":
            self._next_char()
            return Token(self._filename, self._line, cur_col, self._content, TokenType.RIGHT_INDEX)
        raise Exception(f"Error: {self._filename}:{self._line}:{self._col}: Unknown character")
    
    def _append(self):
        self._content += self._cur_char()
    
    def _append_lower(self):
        self._content += self._cur_char().lower()
    
    def _next_char(self):
        self._col += 1
    
    def _cur_char(self) -> str:
        return self._src_code[self._col] if self._col < len(self._src_code) else "\0"

    def _is_same_char(self, c: str) -> bool:
        return self._cur_char() == c
    
    def _is_digit(self) -> bool:
        return self._cur_char().isdigit()
    
    def _is_symbol(self) -> bool:
        return self._cur_char().isdigit() or self._cur_char().isalpha() or self._cur_char() == "_" or self._cur_char() == "."
    
    def _is_hex(self) -> bool:
        return self._is_digit() or 'A' <= self._cur_char() <= 'F' or 'a' <= self._cur_char() <= 'f'
