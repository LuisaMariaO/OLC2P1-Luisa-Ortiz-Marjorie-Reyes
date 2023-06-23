from ..Abstract.instruction import Instruction
from ..Symbol.type import *

class Array(Instruction):
    def __init__(self, id, position, linea, columna):
        self.id = id
        self.position = position
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))
    
    def interpretar(self, arbol, tabla):
        valor = self.id.interpretar(arbol, tabla)
        if type(valor) == Exception:
            return valor
        
        if type(valor) == list and type(self.position) == list:
            for elem in self.position:
                elem = elem.interpretar(arbol, tabla)
                if type(elem) == Exception:
                    return elem
                elem = int(elem)
                if len(valor) > elem:
                    valor = valor[elem]
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
            elif type(valor) == list:
                self.tipoDato = Type(DataType.VECTOR_ANY)
            elif type(valor) == None:
                self.tipoDato = Type(DataType.NULL)
            elif type(valor) == any:
                self.tipoDato = Type(DataType.ANY)
            else:
                return Exception("Error semántico: ", "Tipo de dato inválido", self.linea, self.columna)
            return valor
        else: 
            return Exception("Error semántico", "Acceso a array inválido", self.linea, self.columna)