from ..Abstract.instruction import Instruction
from ..Symbol.type import *
from ..Exceptions.exception import *

class Atributo(Instruction):
    def __init__(self,id,atributo,linea,columna):
        self.id = id
        self.atributo = atributo
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def getValor(self):
        return self.valor
    
    def interpretar(self, arbol, tabla):
        tablaActual = tabla
            
        while (tablaActual!=None):
            busqueda = tablaActual.getSimbolo(self.id.valor)
              
            if busqueda!=None:
                    #Se encontró una variable con ese nombre
                if type(busqueda.getValor().get(self.atributo))==str:
                    self.tipoDato = Type(DataType.STRING)
                elif type(busqueda.getValor().get(self.atributo))==bool:
                    self.tipoDato = Type(DataType.BOOLEAN)
                elif type(busqueda.getValor().get(self.atributo))==int or type(busqueda.getValor().get(self.atributo))==float:
                    self.tipoDato = Type(DataType.NUMBER)
                
                    #print(busqueda.getValor())
                return busqueda.getValor().get(self.atributo)
            tablaActual = tablaActual.getTablaAnterior()
            return Exception("Semántico","No existe una variable o función con el nombre <"+self.valor+">",self.linea,self.columna)
        