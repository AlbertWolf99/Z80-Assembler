class AsmOutput:
    def __init__(self, filename: str):
        self._filename = filename
        self._output_file = open(filename, 'wb')
    
    def output_byte(self, value: int):
        self._output_file.write(value.to_bytes(1, 'little'))