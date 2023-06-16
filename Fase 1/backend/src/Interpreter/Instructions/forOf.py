from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbolTable import *
from ..Symbol.symbol import *
import copy

class ForOf(Instruction):
    def __init__(self,id,iterativo,instrucciones,linea,columna):
        self.id = id
        self.iterativo = iterativo
        self.instrucciones = instrucciones

        super().__init__(linea,columna,Type(DataType.INDEFINIDO)) 

    def interpretar(self, arbol, tabla):
        
        tablaNueva = SymbolTable(tabla,"For")
        valueIterate = self.iterativo.interpretar(arbol,tabla)
        print(valueIterate)
        if type(valueIterate)==Exception: return valueIterate
        
        
        if self.iterativo.tipoDato.getTipo() != DataType.STRING and self.iterativo.tipoDato.getTipo()!=DataType.VECTOR_ANY and self.iterativo.tipoDato.getTipo()!=DataType.VECTOR_BOOLEAN and self.iterativo.tipoDato.getTipo()!=DataType.VECTOR_ID and self.iterativo.tipoDato.getTipo()!=DataType.VECTOR_BOOLEAN and self.iterativo.tipoDato.getTipo()!=DataType.VECTOR_STRING :
           
            return Exception("Semántico","Solo se pueden iterar vectores y strings",self.linea,self.columna)
        
        print(valueIterate)
        tablaNueva.setValor(self.id,Symbol(DataType.INDEFINIDO,self.id,None,"Variable local for",tablaNueva.ambito))
        print(tablaNueva)   

        
        while(len(valueIterate)>0):
            #Actualizo el valor de la variable con el primer elemento del arrego o string
            simbolo = tablaNueva.getSimbolo(self.id)
            simbolo.setValor(valueIterate[0])
            if type(valueIterate[0])==int or type(valueIterate[0])==float:
                simbolo.setTipo(DataType.NUMBER)
            elif type(valueIterate[0])==str:
                simbolo.setTipo(DataType.STRING)
            elif type(valueIterate[0]) == bool:
                simbolo.setTipo(DataType.BOOLEAN)
            #TODO: Agregar la iteración de arreglos de arreglos
            valueIterate = valueIterate[1:]
            
            instruccionesLocales = copy.deepcopy(self.instrucciones)
            for instruccion in instruccionesLocales:
                result = instruccion.interpretar(arbol,tablaNueva)
                if type(result)==Exception:
                    arbol.updateErrores(result)
            
            