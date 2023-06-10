from enum import Enum
from ..Abstract.instruction import Instruction
from ..Symbol.type import *

class Logic:
    def __init__(self,operacion):
        self.operacion = operacion

    def getTipo(self):
        return self.operacion
    
    def setTipo(self,operacion):
        self.operacion = operacion

class LogicType(Enum):
    OR = 1
    AND = 2
    NOT = 3

class Logica(Instruction):
    def __init__(self, izq, der, operacion, linea, columna):
        self.izq = izq
        self.der = der 
        self.operacion = operacion
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))
    
    def interpretar(self, arbol, tabla):
        izq = self.izq.interpretar(arbol, tabla)
        der = self.der.interpretar(arbol, tabla)

        if self.operacion.getTipo() == LogicType.OR:
            if self.izq.tipoDato.getTipo() == DataType.BOOLEAN:
                if self.der.tipoDato.getTipo() == DataType.BOOLEAN:
                    self.tipoDato = DataType.BOOLEAN
                    return (izq or der)
                else: 
                    return None
            else:
                return None
                
        elif self.operacion.getTipo() == LogicType.AND:
            if self.izq.tipoDato.getTipo() == DataType.BOOLEAN:
                if self.der.tipoDato.getTipo() == DataType.BOOLEAN:
                    self.tipoDato = DataType.BOOLEAN
                    return (izq and der)
                else: 
                    return None
            else:
                return None

        elif self.operacion.getTipo() == LogicType.NOT:
            if self.izq.tipoDato.getTipo() == DataType.BOOLEAN:
                if self.der.tipoDato.getTipo() == DataType.BOOLEAN:
                    self.tipoDato = DataType.BOOLEAN
                    return (not izq)
                else: 
                    return None
            else:
                return None
            
        else:
            return None
