class AsmOutput:
    def __init__(self, filename: str):
        self.__filename = filename
        self.__output_file = open(filename, 'wb')
    
    def output_byte(self, value: int):
        self.__output_file.write(value.to_bytes(1, 'little'))