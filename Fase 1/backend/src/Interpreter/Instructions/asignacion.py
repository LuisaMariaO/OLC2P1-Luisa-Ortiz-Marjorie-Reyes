from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbol import Symbol

class Asignacion(Instruction):
    def __init__(self,id,valor,linea,columna):
        self.id = id
        self.valor = valor
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def interpretar(self, arbol, tabla):
        tablaActual = tabla
        while (tablaActual!=None):
            busqueda = tablaActual.getSimbolo(self.id)
            
            if busqueda!=None:
                #Se encontró una variable con ese nombre
                valor = self.valor.interpretar(arbol,tabla)
                if type(valor) == Exception:
                    return valor
                
                if busqueda.getTipo() == self.valor.tipoDato.getTipo() or busqueda.getTipo()==DataType.ANY:
                 
                    busqueda.setValor(valor)
              
                else:
                    return Exception("Semántico","El tipo de dato signado no coincide con el tipo de dato de la variable",self.linea,self.columna)
                
            tablaActual = tablaActual.getTablaAnterior()

        return Exception("Semántico","No existe una variable o función con el nombre <"+self.id+">",self.linea,self.columna)