from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception

class Imprimir(Instruction):
    def __init__(self,tipo,expresiones,linea,columna):
        self.expresiones = expresiones
        super().__init__(linea,columna,tipo)

    def interpretar(self, arbol, tabla):
        valor = ""
        for expresion in self.expresiones:
            result = expresion.interpretar(arbol,tabla)
            if type(result) == Exception:
                return result
            valor+=(str(result))+" "
        arbol.updateConsola(valor)

