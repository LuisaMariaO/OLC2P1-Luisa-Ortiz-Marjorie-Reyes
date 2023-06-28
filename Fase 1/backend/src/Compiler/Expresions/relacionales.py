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
            if self.operacion.getTipo() == RelationalType.IGUAL or self.operacion.getTipo() == RelationalType.DIFERENTE:
                generador.fcompareString()
                paramTemp = generador.addTemp()
                generador.addExp(paramTemp,'P',tabla.size,'+')
                generador.addExp(paramTemp,paramTemp,'1','+')
                generador.setStack(paramTemp,izq.getValue())

                generador.addExp(paramTemp,paramTemp,'1','+')
                generador.setStack(paramTemp,der.getValue())

                generador.newEnv(tabla.size)
                generador.callFun('compareString')

                temp = generador.addTemp()
                generador.getStack(temp,'P')
                generador.retEnv(tabla.size)

                self.checkLabels()
                generador.addIf(temp,self.getNum(),"==",self.getTrueLbl()) #La operación se hará siempre con igual, si es un '===' se compara con true y si es '!=' con false
                generador.addGoto(self.getFalseLbl()) 

               
            else:
                generador.addComment("Error: Operación relacional incompatible con el tipo de dato string")
                return Exception("Semántico","Operación relacional incompatible con el tipo de dato string",self.linea,self.columna)
            
        else:
            generador.addComment("Error: Operación relacional incompatible con el tipo de dato")
            return Exception("Semántico","Operación relacional incompatible con el tipo de dato",self.linea,self.columna)
        
        generador.addComment("FIN DE LA EXPRESION RELACIONAL")
        generador.addSpace()
        result.setTrueLbl(self.trueLbl)
        result.setFalseLbl(self.falseLbl)
        self.tipoDato = Type(DataType.BOOLEAN)
        return result   
        
    def checkLabels(self):
        genAux = Generador()
        generador = genAux.getInstance()

        if self.trueLbl == '':
            self.trueLbl = generador.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generador.newLabel()

    def getNum(self):
        if self.operacion.getTipo()==RelationalType.IGUAL:
            return '1'
        if self.operacion.getTipo()==RelationalType.DIFERENTE:
            return '0'

        