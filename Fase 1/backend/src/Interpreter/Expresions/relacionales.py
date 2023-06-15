from enum import Enum
from ..Abstract.instruction import Instruction
from ..Symbol.type import *

class Relational:
    def __init__(self,operacion):
        self.operacion = operacion

    def getTipo(self):
        return self.operacion
    
    def setTipo(self,operacion):
        self.operacion = operacion

class RelationalType(Enum):
    MAYOR = 1
    MENOR = 2
    IGUAL = 3
    DIFERENTE = 4
    MAYORIGUAL = 5
    MENORIGUAL = 6

class Relacional(Instruction):
    def __init__(self, izq, der, operacion, linea, columna):
        self.izq = izq
        self.der = der 
        self.operacion = operacion
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))
    
    def interpretar(self, arbol, tabla):
        izq = self.izq.interpretar(arbol, tabla)
        der = self.der.interpretar(arbol, tabla)
        

        if self.operacion.getTipo() == RelationalType.MAYOR:
            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq > der)
                else:
                    return Exception("Semántico", "El operador '>' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
            elif self.izq.tipoDato.getTipo() == DataType.STRING:
                if self.der.tipoDato.getTipo() == DataType.STRING:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq > der)
                else:
                    return Exception("Semántico", "El operador '>' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
                
            elif self.izq.tipoDato.getTipo() == DataType.BOOLEAN:
                if self.der.tipoDato.getTipo() == DataType.BOOLEAN:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq > der)
                else:
                    return Exception("Semántico", "El operador '>' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            else:
                return Exception("Semántico", "El operador '>' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
        if self.operacion.getTipo() == RelationalType.MENOR:
            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                   
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq < der)
                else:
                    return Exception("Semántico", "El operador '<' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
            elif self.izq.tipoDato.getTipo() == DataType.STRING:
                if self.der.tipoDato.getTipo() == DataType.STRING:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq < der)
                else:
                    return Exception("Semántico", "El operador '<' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
                
            elif self.izq.tipoDato.getTipo() == DataType.BOOLEAN:
                if self.der.tipoDato.getTipo() == DataType.BOOLEAN:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq < der)
                else:
                    return Exception("Semántico", "El operador '<' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            else:
                return Exception("Semántico", "El operador '<' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
        
        if self.operacion.getTipo() == RelationalType.IGUAL:
            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq == der)
                else:
                    return Exception("Semántico", "El operador '===' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
            elif self.izq.tipoDato.getTipo() == DataType.STRING:
                if self.der.tipoDato.getTipo() == DataType.STRING:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq == der)
                else:
                    return Exception("Semántico", "El operador '===' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
                
            elif self.izq.tipoDato.getTipo() == DataType.BOOLEAN:
                if self.der.tipoDato.getTipo() == DataType.BOOLEAN:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq == der)
                else:
                    return Exception("Semántico", "El operador '===' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            else:
                return Exception("Semántico", "El operador '===' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
        
        if self.operacion.getTipo() == RelationalType.DIFERENTE:
            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq != der)
                else:
                    return Exception("Semántico", "El operador '!==' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
            elif self.izq.tipoDato.getTipo() == DataType.STRING:
                if self.der.tipoDato.getTipo() == DataType.STRING:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq != der)
                else:
                    return Exception("Semántico", "El operador '!==' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
                
            elif self.izq.tipoDato.getTipo() == DataType.BOOLEAN:
                if self.der.tipoDato.getTipo() == DataType.BOOLEAN:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq != der)
                else:
                    return Exception("Semántico", "El operador '!==' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            else:
                return Exception("Semántico", "El operador '!==' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
        
        if self.operacion.getTipo() == RelationalType.MAYORIGUAL:
            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq >= der)
                else:
                    return Exception("Semántico", "El operador '>=' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
            elif self.izq.tipoDato.getTipo() == DataType.STRING:
                if self.der.tipoDato.getTipo() == DataType.STRING:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq >= der)
                else:
                    return Exception("Semántico", "El operador '>=' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
                
            elif self.izq.tipoDato.getTipo() == DataType.BOOLEAN:
                if self.der.tipoDato.getTipo() == DataType.BOOLEAN:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq >= der)
                else:
                    return Exception("Semántico", "El operador '>=' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            else:
                return Exception("Semántico", "El operador '>=' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
        
        if self.operacion.getTipo() == RelationalType.MENORIGUAL:
            if self.izq.tipoDato.getTipo() == DataType.NUMBER:
                if self.der.tipoDato.getTipo() == DataType.NUMBER:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq <= der)
                else:
                    return Exception("Semántico", "El operador '<=' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            
            elif self.izq.tipoDato.getTipo() == DataType.STRING:
                if self.der.tipoDato.getTipo() == DataType.STRING:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq <= der)
                else:
                    return Exception("Semántico", "El operador '<=' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
                
            elif self.izq.tipoDato.getTipo() == DataType.BOOLEAN:
                if self.der.tipoDato.getTipo() == DataType.BOOLEAN:
                    self.tipoDato = Type(DataType.BOOLEAN)
                    return (izq <= der)
                else:
                    return Exception("Semántico", "El operador '<=' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
            else:
                return Exception("Semántico", "El operador '<=' no puede ser aplicado a los tipos '" + self.izq.tipoDato.getTipo() + "' y '"  + self.der.tipoDato.getTipo() + "'", self.linea, self.columna)
        
        else:
            return Exception("Semántico", "El operador '" + self.operacion.tipoDato.getTipo() + "' no es válido", self.linea, self.columna)