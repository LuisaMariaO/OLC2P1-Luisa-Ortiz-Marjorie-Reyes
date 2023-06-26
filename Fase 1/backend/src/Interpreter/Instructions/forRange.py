from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbolTable import *
from ..Symbol.symbol import *
from ..Instructions.breakIns import *
from ..Instructions.continueIns import *
from ..Expresions.returnIns import *
import copy

class ForRange(Instruction):
    def __init__(self,id,valorDeclaracion,condicion,incremental,instrucciones,linea,columna):
        self.id = id
        self.valorDeclaracion = valorDeclaracion 
        self.condicion = condicion
        self.incremental = incremental
        self.instrucciones = instrucciones

        super().__init__(linea,columna,Type(DataType.INDEFINIDO)) 

    def interpretar(self, arbol, tabla):
       
        tablaNueva = SymbolTable(tabla,"For")
        valueDec = self.valorDeclaracion.interpretar(arbol,tabla)
        if type(valueDec)==Exception: return valueDec

        if self.valorDeclaracion.tipoDato.getTipo() != DataType.NUMBER:
            return Exception("Error semántico","Los índices de for deben ser valores numéricos enteros",self.linea,self.columna)
        
        
        tablaNueva.setValor(self.id,Symbol(self.valorDeclaracion.tipoDato.getTipo(),self.id,valueDec,"Variable local for",tablaNueva.ambito,self.linea,self.columna))
       

        condicionCopy = copy.deepcopy(self.condicion)
        
        condition = condicionCopy.interpretar(arbol,tablaNueva)
        
        if condicionCopy.tipoDato.getTipo()!=DataType.BOOLEAN:
            return Exception("Error semántico","La condición debe ser una expresión booleana",self.linea,self.columna)
        if type(condition)==Exception: return condition

        while(condition):
            parar=False
            instruccionesLocales = copy.deepcopy(self.instrucciones)
            for instruccion in instruccionesLocales:
                if isinstance(instruccion,Break):
                    parar=True
                    break
                if isinstance(instruccion,Continue):
                    break
                if isinstance(instruccion,Return):
                    arbol.updateErrores(Exception("Error semántico","La instrucción return no es propia de la instrucción for",self.linea,self.columna))
                    continue
                result = instruccion.interpretar(arbol,tablaNueva)
                if isinstance(result, Return):
                    return result
                if type(result)==Exception:
                    arbol.updateErrores(result)
            if parar:
                break
            #Actualizo el valor de la variable con la incremental
            simbolo = tablaNueva.getSimbolo(self.id)
            valueAc = simbolo.getValor()
            if self.incremental=='+':
                simbolo.setValor(valueAc+1)
            else:
                simbolo.setValor(valueAc-1)
            condicionCopy = copy.deepcopy(self.condicion)
            condition = condicionCopy.interpretar(arbol,tablaNueva)
       
            if condicionCopy.tipoDato.getTipo()!=DataType.BOOLEAN:
                return Exception("Error semántico","La condición debe ser una expresión booleana",self.linea,self.columna)
            if type(condition)==Exception: return condition
