from enum import Enum
from ..Abstract.instruction import Instruction
from ..Symbol.type import *
from ..Symbol.generador import *
from ..Abstract.returnF2 import Return
from ..Exceptions.exception import Exception

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
    
    def compilar(self, arbol, tabla):

        genAux = Generador()
        generador = genAux.getInstance()
        generador.addComment("EXPRESION RELACIONAL")
        izq = self.izq.compilar(arbol, tabla)
        der = self.der.compilar(arbol, tabla)
        
        result = Return(None,Type(DataType.BOOLEAN),False)

        if self.izq.tipoDato.getTipo() == DataType.NUMBER and self.der.tipoDato.getTipo() == DataType.NUMBER:
            self.checkLabels()
            if self.operacion.getTipo() == RelationalType.MAYOR:
                generador.addIf(izq.getValue(),der.getValue(),'>',self.getTrueLbl())
            elif self.operacion.getTipo() == RelationalType.MENOR:
                generador.addIf(izq.getValue(),der.getValue(),'<',self.getTrueLbl())
            elif self.operacion.getTipo() == RelationalType.MAYORIGUAL:
                generador.addIf(izq.getValue(),der.getValue(),'>=',self.getTrueLbl())
            elif self.operacion.getTipo() == RelationalType.MENORIGUAL:
                generador.addIf(izq.getValue(),der.getValue(),'<=',self.getTrueLbl())
            elif self.operacion.getTipo() == RelationalType.IGUAL:
                generador.addIf(izq.getValue(),der.getValue(),'==',self.getTrueLbl())
            elif self.operacion.getTipo() == RelationalType.DIFERENTE:
                generador.addIf(izq.getValue(),der.getValue(),'!=',self.getTrueLbl())
            generador.addGoto(self.getFalseLbl())
        elif self.izq.tipoDato.getTipo() == DataType.STRING and self.der.tipoDato.getTipo() == DataType.STRING:
            pass
            generador.addComment("FIN DE LA EXPRESION RELACIONAL")
            generador.addSpace()
            result.setTrueLbl(self.trueLbl)
            result.setFalseLbl(self.falseLbl)
            self.tipoDato = Type(DataType.BOOLEAN)
            return result
        else:
            generador.addComment("Error: Solo se permiten operaciones relacionales entre valores numéricos")
            return Exception("Semántico","Solo se permiten las operaciones relacionales entre valores numéricos",self.linea,self.columna)
        
    def checkLabels(self):
        genAux = Generador()
        generador = genAux.getInstance()

        if self.trueLbl == '':
            self.trueLbl = generador.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generador.newLabel()

        