from asm.asm_output import AsmOutput
from asm.asm_scanner import AsmScanner
from asm.asm_token import TokenType

class AsmParser:
    NO_ARGS_COMMANDS = {
        "nop":  0b00000000,
        "rlca": 0b00000111,
        "rrca": 0b00001111,
        "rla":  0b00010111,
        "rra":  0b00011111,
        "daa":  0b00100111,
        "cpl":  0b00101111,
        "scf":  0b00110111,
        "ccf":  0b00111111,
        "halt": 0b01110110,
        "exx":  0b11011001,
        "di":   0b11110011,
        "ei":   0b11111011
    }

    def __init__(self, scanner: AsmScanner, output: AsmOutput):
        self.__scanner = scanner
        self.__output = output

    def parse(self):
        while True:
            self._parse_line()
            self.__scanner.next_line()
            if self.__scanner.is_eof():
                break
    
    def _parse_line(self):
        token = self.__scanner.scan()
        if token.type == TokenType.SYMBOL:
            if token.content in self.NO_ARGS_COMMANDS:
                self._parse_no_args(self.NO_ARGS_COMMANDS[token.content])

    def _parse_no_args(self, opcode: int):
        token = self.__scanner.scan()
        if token.type != TokenType.EOL:
            raise Exception(f"Error: {token.filename}:{token.line}:{token.col}: End of Line Expected")
        self.__output.output_byte(opcode)    

    

