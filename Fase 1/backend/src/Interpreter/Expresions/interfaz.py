from ..Abstract.instruction import Instruction
from ..Symbol.type import *

class Interfaz(Instruction):
    def __init__(self, atributos, linea, columna):
        self.atributos = atributos
        super().__init__(linea,columna,Type(DataType.INTERFACE))
    
    def interpretar(self, arbol, tabla):
        if type(self.atributos) == dict:
            for id,val in self.atributos.items():
                if val != DataType.ANY:
                    self.atributos[id] = val.interpretar(arbol, tabla)
                else:
                    tablaActual = tabla
                    while (tablaActual != None):
                        simbolo = tablaActual.getSimbolo(id)
                        if simbolo!=None:
                            self.atributos[id] = simbolo
                            break
                        tablaActual = tablaActual.getTablaAnterior()
            return self.atributos