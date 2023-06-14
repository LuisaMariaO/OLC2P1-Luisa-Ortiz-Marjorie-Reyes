from enum import Enum
from ..Abstract.instruction import Instruction
from ..Symbol.type import *

class Aritmetic:
    def __init__(self,operacion):
        self.operacion = operacion

    def getTipo(self):
        return self.operacion
    
    def setTipo(self,operacion):
        self.operacion = operacion

class AritmeticType(Enum):
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    POTENCIA = 5
    MODULO = 6
    NEGACION = 7

class Aritmetica(Instruction):
    def __init__(self, izq, der, operacion, linea, columna):
        self.izq = izq
        self.der = der 
        self.operacion = operacion
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))
    
    def interpretar(self, arbol, tabla):
        izq = self.izq.interpretar(arbol, tabla)
        der = self.der.interpretar(arbol, tabla)

        if self.operacion.getTipo() == AritmeticType.SUMA:
            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                    self.tipoDato = Type(DataType.NUMBER)
                    return (izq + der)
                elif self.der.tipoDato.getTipo() == DataType.STRING:
                    self.tipoDato = Type(DataType.STRING)
                    return (str(izq) + der)
                else:
                    return Exception("Semántico", "El operador '+' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
            if self.izq.tipoDato.getTipo() == DataType.STRING:
                if self.der.tipoDato.getTipo() == DataType.STRING:
                    self.tipoDato = Type(DataType.STRING)
                    return (izq + der)
                elif self.der.tipoDato.getTipo() == DataType.NUMBER:
                    self.tipoDato = Type(DataType.STRING)
                    return (izq + str(der))
                else:
                    return Exception("Semántico", "El operador '+' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
            else:
                return Exception("Semántico", "El operador '+' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
                
        elif self.operacion.getTipo() == AritmeticType.RESTA:
            izq = self.izq.interpretar(arbol, tabla)
            der = self.der.interpretar(arbol, tabla)

            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                    self.tipoDato = Type(DataType.NUMBER)
                    return (izq - der)
                else:
                    return Exception("Semántico", "El operador '-' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            else: 
                return Exception("Semántico", "El operador '-' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
        elif self.operacion.getTipo() == AritmeticType.MULTIPLICACION:
            izq = self.izq.interpretar(arbol, tabla)
            der = self.der.interpretar(arbol, tabla)

            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                    self.tipoDato = Type(DataType.NUMBER)
                    return (izq * der)
                else:
                    return Exception("Semántico", "El operador '*' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            else: 
                return Exception("Semántico", "El operador '*' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
        elif self.operacion.getTipo() == AritmeticType.DIVISION:
            izq = self.izq.interpretar(arbol, tabla)
            der = self.der.interpretar(arbol, tabla)

            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                    if der == 0:
                        return Exception("Semántico", "División sobre 0", self.linea, self.columna)
                    else:
                        self.tipoDato = Type(DataType.NUMBER)
                        return (izq / der)
                else:
                    return Exception("Semántico", "El operador '/' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            else: 
                return Exception("Semántico", "El operador '/' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
        elif self.operacion.getTipo() == AritmeticType.POTENCIA:
            izq = self.izq.interpretar(arbol, tabla)
            der = self.der.interpretar(arbol, tabla)

            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                    self.tipoDato = Type(DataType.NUMBER)
                    return pow(izq, der)
                else:
                    return Exception("Semántico", "El operador '^' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            else: 
                return Exception("Semántico", "El operador '^' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
        
        elif self.operacion.getTipo() == AritmeticType.MODULO:
            izq = self.izq.interpretar(arbol, tabla)
            der = self.der.interpretar(arbol, tabla)

            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                    self.tipoDato = Type(DataType.NUMBER)
                    return (izq % der)
                else:
                    return Exception("Semántico", "El operador '%' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            else: 
                return Exception("Semántico", "El operador '%' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
        
        else:
            return Exception("Semántico", "El operador '" + self.operacion.getTipo() + "' no es válido", self.linea, self.columna)

