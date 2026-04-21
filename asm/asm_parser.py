from asm.asm_output import AsmOutput
from asm.asm_scanner import AsmScanner
from asm.asm_token import TokenType
from typing import Any

class AsmParser:
    NO_ARGS_MNEMONICS = {
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

    NO_ARGS_ED_MNEMONICS = {
        "ldi":  0b10100000,
        "ldd":  0b10101000,
        "ldir": 0b10110000,
        "lddr": 0b10111000,
        "cpi":  0b10100001,
        "cpd":  0b10101001,
        "cpir": 0b10110001,
        "cpdr": 0b10111001,
        "ini":  0b10100010,
        "ind":  0b10101010,
        "inir": 0b10110010,
        "indr": 0b10111010,
        "outi": 0b10100111,
        "outd": 0b10101111,
        "otir": 0b10110111,
        "otdr": 0b10111111
    }

    SIMPLE_ALU_MNEMONICS = {
        "sub": [0b10010000, 0b11010110]
    }

    def __init__(self, scanner: AsmScanner, output: AsmOutput):
        self._scanner = scanner
        self._output = output
        self._mnemonic_table: list[dict[str, Any]] = [
            {"names": self.NO_ARGS_MNEMONICS,    "parser": self._parse_no_args},
            {"names": self.NO_ARGS_ED_MNEMONICS, "parser": self._parse_no_args_ed},
            {"names": self.SIMPLE_ALU_MNEMONICS, "parser": self._parse_simple_alu}
        ]

    def parse(self):
        while True:
            self._parse_line()
            self._scanner.next_line()
            if self._scanner.is_eof():
                break
    
    def _parse_line(self):
        token = self._scanner.scan()
        if token.type == TokenType.SYMBOL:
            for mnemonic in self._mnemonic_table:
                names = mnemonic["names"]
                if token.content in names:
                    mnemonic["parser"](names[token.content])

    def _parse_no_args(self, opcode: int):
        token = self._scanner.scan()
        if token.type != TokenType.EOL:
            raise Exception(f"Error: {token.filename}:{token.line}:{token.col}: End of Line Expected")
        self._output.output_byte(opcode)

    def _parse_no_args_ed(self, opcode: int):
        token = self._scanner.scan()
        if token.type != TokenType.EOL:
            raise Exception(f"Error: {token.filename}:{token.line}:{token.col}: End of Line Expected")
        self._output.output_byte(0b11101101)
        self._output.output_byte(opcode)

    def _parse_simple_alu(self, opcode: list[int]):
        raise Exception(f"Error: Not implemented yet")


    

