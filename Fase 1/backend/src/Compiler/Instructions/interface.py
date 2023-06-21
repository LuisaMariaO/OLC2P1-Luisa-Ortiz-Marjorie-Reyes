from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbol import Symbol

class Interface(Instruction):
    def __init__(self,id,campos,linea,columna):
        self.id = id
        self.campos = campos
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def getParametros(self):
        return self.campos
    
    def interpretar(self, arbol, tabla):
        tablaActual = tabla
        while (tablaActual!=None):
            busqueda = tablaActual.getSimbolo(self.id)
               
            if busqueda!=None:
                #Se encontró una funcion con ese nombre
                return Exception("Semántico","Ya existe una variable, función o interface con el nombre <"+self.id+">",self.linea,self.columna)
                 
                
              
            tablaActual = tablaActual.getTablaAnterior()
             
        
        tabla.setValor(self.id,Symbol(DataType.INTERFACE,self.id,self,"Interface",tabla.ambito))
        