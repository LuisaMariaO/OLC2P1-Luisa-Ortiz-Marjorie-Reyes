from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbolTable import *
import copy
from ..Instructions.continueIns import *
from ..Instructions.breakIns import *
from ..Expresions.returnIns import *

class While(Instruction):
    def __init__(self,condicion,instrucciones,linea,columna):
        self.condicion = condicion
        self.instrucciones = instrucciones

        super().__init__(linea,columna,Type(DataType.INDEFINIDO)) 

    def interpretar(self, arbol, tabla):
        condicionCopy = copy.deepcopy(self.condicion)
        condition = condicionCopy.interpretar(arbol,tabla)

       
        if condicionCopy.tipoDato.getTipo()!=DataType.BOOLEAN:
            return Exception("Error semántico","La condición debe ser una expresión booleana",self.linea,self.columna)
        if type(condition)==Exception: return condition
        tablaNueva = SymbolTable(tabla,"While")
        while(condition):
            parar = False
            instruccionesLocales = copy.deepcopy(self.instrucciones)
            for instruccion in instruccionesLocales:
                if type(instruccion)==Break:
                    parar = True
                    break
                if isinstance(instruccion,Continue):
                    break
                if isinstance(instruccion,Return):
                    arbol.updateErrores(Exception("Error semántico","La instrucción return no es propia de la instrucción for",self.linea,self.columna))
                    continue
                result = instruccion.interpretar(arbol,tablaNueva)
                if type(result)==Exception:
                    arbol.updateErrores(result)
            if parar:
                break
            condicionCopy = copy.deepcopy(self.condicion)
            condition = condicionCopy.interpretar(arbol,tabla)
       
            if condicionCopy.tipoDato.getTipo()!=DataType.BOOLEAN:
                return Exception("Error semántico","La condición debe ser una expresión booleana",self.linea,self.columna)
            if type(condition)==Exception: return condition



