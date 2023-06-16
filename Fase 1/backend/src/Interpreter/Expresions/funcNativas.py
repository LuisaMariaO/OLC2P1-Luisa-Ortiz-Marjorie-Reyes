from enum import Enum
from ..Abstract.instruction import Instruction
from ..Symbol.type import *

class Native:
    def __init__(self,funcion):
        self.funcion = funcion

    def getTipo(self):
        return self.funcion
    
    def setTipo(self,funcion):
        self.funcion = funcion

class NativeFunc(Enum):
    FIXED = 1
    EXPO = 2
    STRING = 3
    LOWER = 4
    UPPER = 5
    SPLIT = 6
    CONCAT = 7

class FuncionNativa(Instruction):
    def __init__(self, op, func, parametro, linea, columna):
        self.op = op
        self.func = func
        self.parametro = parametro
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))
    
    def interpretar(self, arbol, tabla):
        op = self.op.interpretar(arbol, tabla)
        
        if self.func.getTipo() == NativeFunc.FIXED:
            if self.op.tipoDato.getTipo() == DataType.NUMBER:
                self.tipoDato = Type(DataType.NUMBER)
                if self.parametro != None:
                    p = self.parametro.interpretar(arbol, tabla)
                    return round(op, int(p))
                else:
                    return int(round(op, 0))
            else:
                return Exception("Semántica", "Tipo de dato no válido para la función 'toFixed'", self.linea, self.columna)

        elif self.func.getTipo() == NativeFunc.EXPO:
            if self.op.tipoDato.getTipo() == DataType.NUMBER:
                self.tipoDato = Type(DataType.NUMBER)
                if self.parametro != None:
                    p = self.parametro.interpretar(arbol, tabla)
                    structure = "." + str(int(p)) + "E"
                    return format(op, str(structure))
                else:
                    return format(op, '.1E')
            else:
                return Exception("Semántica", "Tipo de dato no válido para la función 'toExponential'", self.linea, self.columna)

        elif self.func.getTipo() == NativeFunc.STRING:
            if self.op.tipoDato.getTipo() == DataType.STRING:
                self.tipoDato = Type(DataType.STRING)
                return str(op)
            elif self.op.tipoDato.getTipo() == DataType.NUMBER:
                self.tipoDato = Type(DataType.STRING)
                return str(op)
            if self.op.tipoDato.getTipo() == DataType.BOOLEAN:
                self.tipoDato = Type(DataType.STRING)
                return str(op)
            else:
                return Exception("Semántica", "Tipo de dato no válido para la función 'toString'", self.linea, self.columna)
            
        elif self.func.getTipo() == NativeFunc.LOWER:
            
            if self.op.tipoDato.getTipo() == DataType.STRING:
                self.tipoDato = Type(DataType.STRING)
                return op.lower()
            else:
                return Exception("Semántica", "Tipo de dato no válido para la función 'toLowerCase", self.linea, self.columna)
        
        elif self.func.getTipo() == NativeFunc.UPPER:
            if self.op.tipoDato.getTipo() == DataType.STRING:
                self.tipoDato = Type(DataType.STRING)
                return op.upper()
            else:
                return Exception("Semántica", "Tipo de dato no válido para la función 'toUpperCase", self.linea, self.columna)

        elif self.func.getTipo() == NativeFunc.SPLIT:
            if self.op.tipoDato.getTipo() == DataType.STRING:
                self.tipoDato = Type(DataType.VECTOR_STRING)
                if self.parametro != None:
                    p = self.parametro.interpretar(arbol, tabla)
                    return op.split(str(p))
                else:
                    return Exception("Semántica", "La función 'split' no cuenta con un parámetro obligatorio", self.linea, self.columna)
            else:
                return Exception("Semántica", "Tipo de dato no válido para la función 'Split", self.linea, self.columna)

        '''elif self.func.getTipo() == NativeFunc.CONCAT:'''

