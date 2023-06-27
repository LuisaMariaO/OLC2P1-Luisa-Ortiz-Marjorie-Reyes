from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception

class Return(Instruction):
    def __init__(self, valor,linea, columna):
        self.valor = valor
        super().__init__(linea, columna, DataType.INDEFINIDO)

    def interpretar(self, arbol, tabla):
        if self.valor!=None:
            '''if type(self.valor) == dict:
                returnValue = {}
                for id in self.valor:
                    tablaActual = tabla
                    while (tablaActual != None):
                        simbolo = tablaActual.getSimbolo(id)
                        if simbolo!=None:
                            returnValue[id] = simbolo
                            break
                        tablaActual = tablaActual.getTablaAnterior()
                self.valor = returnValue
                self.tipoDato = Type(DataType.INTERFACE)
                return self
            else:'''
            returnValue = self.valor.interpretar(arbol,tabla)
            if type(returnValue) == Exception:
                return returnValue
            self.tipoDato = self.valor.tipoDato
            self.valor = returnValue
            return self
        else:
            self.tipoDato = Type(DataType.NULL)
            return self
        

        '''if self.valor!=None:
            returnValue = self.valor.interpretar(arbol,tabla)
            if type(returnValue) == Exception:
                return returnValue
            self.tipoDato = self.valor.tipoDato
            self.valor = returnValue
            return self
        else:
            self.tipoDato = Type(DataType.NULL)
            return self'''