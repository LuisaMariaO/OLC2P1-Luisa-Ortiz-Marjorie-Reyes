from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception

class Return(Instruction):
    def __init__(self, valor,linea, columna):
        self.valor = valor
        super().__init__(linea, columna, DataType.INDEFINIDO)

    def interpretar(self, arbol, tabla):
        if self.valor!=None:
            returnValue = self.valor.interpretar(arbol,tabla)
            if type(returnValue) == Exception:
                return returnValue
            self.tipoDato = self.valor.tipoDato
            return returnValue
        else:
            self.tipoDato = Type(DataType.NULL)
            return None