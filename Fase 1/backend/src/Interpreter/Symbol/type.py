from enum import Enum

class Type:
    def __init__(self,tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo
    
    def setTipo(self,tipo):
        self.tipo = tipo

class DataType(Enum):
    NUMBER = 1
    STRING = 2
    BOOLEAN = 3
    ANY = 4
    NULL = 5
    ID = 6
    VECTOR_NUMBER = 7
    VECTOR_STRING = 8
    VECTOR_BOOLEAN = 9
    VECTOR_ANY = 10
    VECTOR_ID = 11
    INDEFINIDO = 12
    LLAMADA = 13
    