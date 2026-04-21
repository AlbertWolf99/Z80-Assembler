from asm.asm_scanner import AsmScanner
from asm.asm_token import TokenType

class AsmExpr:

    @staticmethod
    def parse_expression(parser: AsmScanner):
        token = parser.get_current_token()
        parser.get_next_token()
        if token.type == TokenType.INTEGER_LITERAL:
            return token.value
        raise Exception(f"Error: {token.filename}:{token.line}:{token.col}: Valid Expression Expected")