from ..Abstract.instruction import Instruction
from ..Symbol.type import *

class Array(Instruction):
    def __init__(self, id, position, linea, columna):
        self.id = id
        self.position = position
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))
    
    def interpretar(self, arbol, tabla):
        valor = self.id.interpretar(arbol, tabla)
        if type(valor) == list and type(self.position) == list:
            for elem in self.position:
                if len(valor) > int(elem.interpretar(arbol, tabla)):
                    valor = valor[int(elem.interpretar(arbol, tabla))]
                    if type(valor) != list:
                        break
                else:
                    return Exception("Error semántico", "Acceso a array inválido", self.linea, self.columna)
            if type(valor) == float:
                self.tipoDato = Type(DataType.NUMBER)
            elif type(valor) == str:
                self.tipoDato = Type(DataType.STRING)
            elif type(valor) == bool:
                self.tipoDato = Type(DataType.BOOLEAN)
            else:
                self.tipoDato = Type(DataType.ANY)
            return valor
        else: 
            return Exception("Error semántico", "Acceso a array inválido", self.linea, self.columna)