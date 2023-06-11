from ..Abstract.instruction import Instruction
from ..Symbol.type import *

class Nativo(Instruction):
    def __init__(self,tipo,valor,linea,columna):
        self.valor = valor
        super().__init__(linea,columna,tipo)

    def getValor(self):
        return self.valor
    
    def interpretar(self, arbol, tabla):

        if self.tipoDato.getTipo() == DataType.NUMBER:
            return float(self.valor)
        elif self.tipoDato.getTipo() == DataType.STRING:
            return self.valor
        elif self.tipoDato.getTipo() == DataType.BOOLEAN:
            if self.valor == 'true':
                return True
            return False
        elif self.tipoDato.getTipo() == DataType.ID:
            tablaActual = tabla
            
            while (tablaActual!=None):
                busqueda = tablaActual.getSimbolo(self.valor)
            
                if busqueda!=None:
                    #Se encontró una variable con ese nombre
                    self.tipoDato = Type(busqueda.getTipo())
                    return busqueda.getValor()
                tablaActual = tablaActual.getTablaAnterior()
            return Exception("Semántico","No existe una variable o función con el nombre <"+self.valor+">",self.linea,self.columna)
