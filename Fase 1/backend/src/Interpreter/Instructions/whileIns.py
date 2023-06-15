from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbolTable import *
import copy

class While(Instruction):
    def __init__(self,condicion,instrucciones,linea,columna):
        self.condicion = condicion
        self.instrucciones = instrucciones

        super().__init__(linea,columna,Type(DataType.INDEFINIDO)) 

    def interpretar(self, arbol, tabla):
        condicionCopy = copy.deepcopy(self.condicion)
        condition = condicionCopy.interpretar(arbol,tabla)

       
        if condicionCopy.tipoDato.getTipo()!=DataType.BOOLEAN:
            return Exception("Semántico","La condición debe ser una expresión booleana",self.linea,self.columna)
        if type(condition)==Exception: return condition
        tablaNueva = SymbolTable(tabla,"While")
        while(condition):
            
            instruccionesLocales = copy.deepcopy(self.instrucciones)
            for instruccion in instruccionesLocales:
                result = instruccion.interpretar(arbol,tablaNueva)
                if type(result)==Exception:
                    arbol.updateErrores(result)

            condicionCopy = copy.deepcopy(self.condicion)
            condition = condicionCopy.interpretar(arbol,tabla)
       
            if condicionCopy.tipoDato.getTipo()!=DataType.BOOLEAN:
                return Exception("Semántico","La condición debe ser una expresión booleana",self.linea,self.columna)
            if type(condition)==Exception: return condition



