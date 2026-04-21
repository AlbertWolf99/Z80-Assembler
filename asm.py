import sys
from asm.asm_output import AsmOutput
from asm.asm_parser import AsmParser
from asm.asm_scanner import AsmScanner

argv = sys.argv

if len(argv) != 3:
    print("Usage: asm.py input_file output_file")
    sys.exit()

input_file = argv[1]
output_file = argv[2]

parser = AsmParser(AsmScanner(input_file), AsmOutput(output_file))
parser.parse()