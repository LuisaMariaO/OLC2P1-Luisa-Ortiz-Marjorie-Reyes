from src.Interpreter.Symbol.type import DataType

class Symbol:
    def __init__(self, tipo, identificador, valor, rol, ambito, fila, columna):
        self.tipo = tipo
        self.identificador = identificador
        self.valor = valor
        self.rol = rol
        self.ambito = ambito
        self.fila = fila
        self.columna = columna

    def getTipo(self):
        return self.tipo
    
    def setTipo(self,tipo):
        self.tipo = tipo

    def getIdentificador(self):
        return self.identificador
    
    def setIdentificador(self, identificador):
        self.identificador = identificador

    def getValor(self):
        return self.valor
    
    def setValor(self,valor):
        self.valor = valor

    def getAmbito(self):
        return self.ambito
    
    def getRol(self):
        return self.rol
    
    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna
    
    def translateTipo(self):
        if self.tipo == DataType.NUMBER:
            return "number"
        elif self.tipo == DataType.STRING:
            return "string"
        elif self.tipo == DataType.BOOLEAN:
            return "boolean"
        elif self.tipo == DataType.ANY:
            return "any"
        elif self.tipo == DataType.NULL:
            return "null"
        elif self.tipo == DataType.VECTOR_ANY:
            return "array"
        elif self.tipo == DataType.INTERFACE:
            return "interface"