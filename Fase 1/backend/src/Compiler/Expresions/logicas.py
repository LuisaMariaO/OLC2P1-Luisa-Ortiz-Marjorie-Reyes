from enum import Enum
from ..Abstract.instruction import Instruction
from ..Symbol.type import *
from ..Symbol.generador import Generador
from ..Exceptions.exception import Exception
from ..Abstract.returnF2 import Return

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
    
    def compilar(self, arbol, tabla):
        genAux = Generador()
        generador = genAux.getInstance()
        generador.addComment("EXPRESION LOGICA")
       

        self.checkLabels()
        lblAndOr = ''

        if self.operacion.getTipo() == LogicType.AND:
            lblAndOr = generador.newLabel()

            self.izq.setTrueLbl(lblAndOr)
            self.der.setTrueLbl(self.trueLbl)
            self.izq.falseLbl = self.der.falseLbl = self.falseLbl

        elif self.operacion.getTipo() == LogicType.OR:
            self.izq.setTrueLbl(self.trueLbl)
            self.der.setTrueLbl(self.trueLbl)

            lblAndOr = generador.newLabel()

            self.izq.setFalseLbl(lblAndOr)
            self.der.setFalseLbl(self.falseLbl)

        elif self.operacion.getTipo() == LogicType.NOT:
            self.izq.setFalseLbl(self.trueLbl)
            self.izq.setTrueLbl(self.falseLbl)
            lblNot =  self.izq.compilar(arbol,tabla)

            lblTrue = lblNot.getTrueLbl()
            lblFalse = lblNot.getFalseLbl()
            lblNot.setTrueLbl(lblFalse)
            lblNot.setFalseLbl(lblTrue)

            self.tipoDato = Type(DataType.BOOLEAN)
            return lblNot
        
        izq = self.izq.compilar(arbol,tabla)
        if isinstance(izq,Exception): return izq
        generador.putLabel(lblAndOr)

        der = self.der.compilar(arbol,tabla)
        if isinstance(der,Exception) : return der
        
        generador.addComment("FIN DE LA EXPRESION LOGICA")
        generador.addSpace()

        ret = Return(None,Type(DataType.BOOLEAN),False)
        ret.setTrueLbl(self.trueLbl)
        ret.setFalseLbl(self.falseLbl)
        self.tipoDato = Type(DataType.BOOLEAN)
        return ret

    def checkLabels(self):
        genAux = Generador()
        generador = genAux.getInstance()

        if self.trueLbl == '':
            self.trueLbl = generador.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generador.newLabel()