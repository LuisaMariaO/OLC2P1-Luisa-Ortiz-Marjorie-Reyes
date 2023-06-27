from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbol import Symbol


class Funcion(Instruction):
    def __init__(self,id,parametros,instrucciones,tipo,linea,columna):
        self.id = id
        self.instrucciones = instrucciones
        self.parametros = parametros
        self.tipo = tipo
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def getInstrucciones(self):
        return self.instrucciones
    
    def getParametros(self):
        return self.parametros

    def interpretar(self, arbol, tabla):
       
        tablaActual = tabla
        while (tablaActual!=None):
            busqueda = tablaActual.getSimbolo(self.id)
               
            if busqueda!=None:
                #Se encontró una funcion con ese nombre
                return Exception("Error semántico","Ya existe una variable o función con el nombre '"+self.id+"'",self.linea,self.columna)
                 
            tablaActual = tablaActual.getTablaAnterior()
        if type(self.tipo) == str:
            self.tipoDato = self.tipo
        tabla.setValor(self.id,Symbol(self.tipoDato,self.id,self,"Función",tabla.ambito,self.linea,self.columna))