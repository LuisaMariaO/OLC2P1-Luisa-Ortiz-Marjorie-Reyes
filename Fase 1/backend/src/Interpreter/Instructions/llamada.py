from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbol import Symbol
from ..Symbol.symbolTable import *
import copy
from ..Expresions.returnIns import *
from ..Instructions.breakIns import *
from ..Instructions.continueIns import *

class Llamada(Instruction):
    def __init__(self,id,parametros,linea,columna):
        self.id = id
        self.parametros = parametros
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def interpretar(self, arbol, tabla):
   
        tablaActual = tabla
        while (tablaActual!=None):
            busqueda = tablaActual.getSimbolo(self.id)
           
            if busqueda!=None:
                #Se encontró una función con ese nombre
                simbolo = tablaActual.getSimbolo(self.id)
                funcion = copy.deepcopy(simbolo.valor)
               
                parametrosDeclaracion = funcion.getParametros()
                
                instrucciones = funcion.getInstrucciones()
                
                #Acá comparo la longitud de las listas de parametros
                if len(parametrosDeclaracion) != len(self.parametros):
                    return Exception("Error semántico","El número de parámetros recibidos no coincide con la función declarada",self.linea,self.columna)
                
                nuevaTabla = SymbolTable(tabla,"Función "+self.id)
                
                #Itero los parámetros de declaración y los recibidos para declarar las variables locales
         
                simbolos = []
                for ide,tipo in parametrosDeclaracion.items():
                    
                    if tipo==None:
                        tipo = DataType.NULL
                    simbolos.append(Symbol(tipo,ide,None,"Parametro",nuevaTabla.ambito,self.linea,self.columna))

                for (simbolo,valor) in zip(simbolos,self.parametros):
                    
                    nuevoValor = valor.interpretar(arbol,tabla)
                    
                    if valor.tipoDato.getTipo() == simbolo.getTipo():
                        simbolo.setValor(nuevoValor)
                        
                        nuevaTabla.setValor(simbolo.identificador,simbolo)
                    else:
                        return Exception("Error semántico","No coinciden los tipos de los parámetros",self.linea,self.columna)
                    
                
                for instruccion in instrucciones:
                    
                    
                    if isinstance(instruccion,Break):
                       
                        arbol.updateErrores(Exception("Error semántico","La instrucción break no es propia de las funciones",self.linea,self.columna))
                        continue
                    if isinstance(instruccion,Continue):
                        arbol.updateErrores(Exception("Error semántico","La instrucción continue no es propia de las funciones",self.linea,self.columna))
                        continue
                    
                    returnValue = instruccion.interpretar(arbol, nuevaTabla)
                    
                    if type(instruccion)== Return or type(returnValue)==Return:
                        
                        self.tipoDato = instruccion.tipoDato
                        return returnValue
                    if type(returnValue)==Exception:
                        arbol.updateErrores(returnValue)
                return None
                
            tablaActual = tablaActual.getTablaAnterior()

        return Exception("Error semántico","No se encontró la función '"+self.id+"'",self.linea,self.columna)

        