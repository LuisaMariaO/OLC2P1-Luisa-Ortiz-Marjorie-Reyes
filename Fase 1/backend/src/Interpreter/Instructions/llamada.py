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
        #Primero se busca en la tabla de símbolos una función con el ID llamado
        tablaActual = tabla
        while (tablaActual!=None):
            busqueda = tablaActual.getSimbolo(self.id)
            if busqueda!=None:
                #Sí encontró una función con ese nombre, se guarda la función, los parámetros e instrucciones
                simbolo = tablaActual.getSimbolo(self.id)
                funcion = copy.deepcopy(simbolo.valor)
                parametrosDeclaracion = funcion.getParametros()
                instrucciones = funcion.getInstrucciones()
                #Acá comparo la longitud de las listas de parametros de la llamada con las de la función declarada
                if len(parametrosDeclaracion) != len(self.parametros):
                    return Exception("Error semántico","El número de parámetros recibidos no coincide con la función declarada",self.linea,self.columna)
                #Se crea una nueva tabla para las variables locales de la función
                nuevaTabla = SymbolTable(tabla,"Función "+self.id)
                simbolos = []
                if len(parametrosDeclaracion) > 0:
                    for ide,tipo in parametrosDeclaracion.items():    
                        if tipo==None:
                            tipo = DataType.NULL
                        simbolos.append(Symbol(tipo,ide,None,"Parametro",nuevaTabla.ambito,self.linea,self.columna))
                    for (simbolo,valor) in zip(simbolos,self.parametros):
                        nuevoValor = valor.interpretar(arbol,tabla)
                        if valor.tipoDato.getTipo() == DataType.VECTOR_ANY:
                            simbolo.setTipo(DataType.VECTOR_ANY)
                        if valor.tipoDato.getTipo() == simbolo.getTipo():
                            simbolo.setValor(nuevoValor)
                            nuevaTabla.setValor(simbolo.identificador,simbolo)
                        else:
                            return Exception("Error semántico","No coinciden los tipos de los parámetros",self.linea,self.columna)
                    
                #Después de declarar los parámetros se recorren las instrucciones
                for instruccion in instrucciones:
                    if isinstance(instruccion,Break):
                        arbol.updateErrores(Exception("Error semántico","La instrucción break no es propia de las funciones",self.linea,self.columna))
                        continue
                    if isinstance(instruccion,Continue):
                        arbol.updateErrores(Exception("Error semántico","La instrucción continue no es propia de las funciones",self.linea,self.columna))
                        continue
                    
                    returnValue = instruccion.interpretar(arbol, nuevaTabla)
                    if isinstance(returnValue, Return):
                        if type(funcion.tipo) == str:
                            return {"valor" : returnValue.valor, "tipo": funcion.tipo}
                        self.tipoDato = returnValue.tipoDato
                        return returnValue.valor
                    '''if type(instruccion)== Return or type(returnValue)==Return:
                        self.tipoDato = instruccion.tipoDato
                        return returnValue'''
                    if type(returnValue)==Exception:
                        arbol.updateErrores(returnValue)
                return None   
            tablaActual = tablaActual.getTablaAnterior()
        return Exception("Error semántico","No se encontró la función '"+self.id+"'",self.linea,self.columna)

        