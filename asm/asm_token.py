from enum import Enum

class TokenType(Enum):
    EOL = 0
    SYMBOL = 1
    INTEGER_LITERAL = 2
    STRING_LITERAL = 3
    COMMA = 4
    LEFT_PARENTHESIS = 5
    RIGHT_PARENTHESIS = 6
    PLUS = 7
    MINUS = 8
    TIMES = 9
    DIVISION = 10
    MODULO = 11
    SHIFT_LEFT = 12
    SHIFT_RIGHT = 13
    START_POSITION = 14
    CURRENT_POSITION = 15


class Token:
    def __init__(self, filename: str, line: int, col: int, content: str, token_type: TokenType, value: int = 0):
        self.filename = filename
        self.line = line
        self.col = col
        self.content = content
        self.type = token_type
        self.value = value
    
    def __str__(self):
        return f"Filename: {self.filename}\nLine: {self.line}\nColumn: {self.col}\nContent: {self.content}\nType: {self.type}\nValue: {self.value}"