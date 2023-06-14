from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception

class Imprimir(Instruction):
    def __init__(self,tipo,expresion,linea,columna):
        self.expresion = expresion
        super().__init__(linea,columna,tipo)

    def interpretar(self, arbol, tabla):

        valor = self.expresion.interpretar(arbol,tabla)
        
        if type(valor) == Exception:
            return valor
        arbol.updateConsola(valor)

