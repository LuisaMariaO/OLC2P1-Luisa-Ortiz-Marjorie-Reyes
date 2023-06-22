from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.generador import *

class Imprimir(Instruction):
    def __init__(self,tipo,expresiones,linea,columna):
        self.expresiones = expresiones
        super().__init__(linea,columna,tipo)

    def compilar(self, arbol, tabla):
        genAux = Generador()
        generador = genAux.getInstance()
       
        for expresion in self.expresiones:
            result = expresion.compilar(arbol,tabla)
            if type(result)== Exception:
                return result
            if expresion.tipoDato.getTipo() == DataType.NUMBER:
                generador.addPrint('f',result.getValue()) #imprimimos siempre floats porque no se manejan por separado enteros y flotantes
            
        
        
        

