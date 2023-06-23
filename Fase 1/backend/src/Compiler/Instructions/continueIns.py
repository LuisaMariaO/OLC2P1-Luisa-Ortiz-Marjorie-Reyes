from ..Abstract.instruction import Instruction
from ..Symbol.type import*
class Continue(Instruction):
    def __init__(self,linea, columna):
       
        super().__init__(linea, columna, DataType.INDEFINIDO)

    def interpretar(self, arbol, tabla):
        pass