from ..Abstract.instruction import Instruction
from ..Symbol.type import *
from ..Abstract.returnF2 import *
from ..Symbol.generador import *

class Nativo(Instruction):
    def __init__(self,tipo,valor,linea,columna):
        self.valor = valor
        super().__init__(linea,columna,tipo)

    def getValor(self):
        return self.valor
    
    def compilar(self, arbol, tabla):
        #TODO: Retorno para variables y llamadas
        genAux = Generador()
        generador = genAux.getInstance()
        return Return(str(self.valor),self.tipoDato,False)