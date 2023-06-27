from ..Abstract.instruction import Instruction
from ..Symbol.type import *
from ..Exceptions.exception import *

def Recorrer(array, arbol, tabla):
    arr = []
    for element in array:
        if isinstance(element,list):
            Recorrer(element, arbol, tabla)
        else:
            element = element.interpretar(arbol, tabla)
            if type(element) == Exception:
                return element
            arr.append(element)
    return arr

class Nativo(Instruction):
    def __init__(self,tipo,valor,linea,columna):
        self.valor = valor
        super().__init__(linea,columna,tipo)

    def getValor(self):
        return self.valor
        
    def interpretar(self, arbol, tabla):
        if self.tipoDato.getTipo() == DataType.NUMBER:
            return float(self.valor)
        elif self.tipoDato.getTipo() == DataType.STRING:
            return self.valor
        elif self.tipoDato.getTipo() == DataType.BOOLEAN:
            if self.valor == 'true':
                return True
            return False
        elif self.tipoDato.getTipo() == DataType.ID:
            tablaActual = tabla
            
            while (tablaActual!=None):
                busqueda = tablaActual.getSimbolo(self.valor)
              
                if busqueda!=None:
                    #Se encontró una variable con ese nombre
                    self.tipoDato = Type(busqueda.getTipo())
                    return busqueda.getValor()
                tablaActual = tablaActual.getTablaAnterior()
            return Exception("Error semántico","No existe una variable o función con el nombre: "+self.valor,self.linea,self.columna)
            
        elif self.tipoDato.getTipo() == DataType.LLAMADA:
            valor = self.valor.interpretar(arbol,tabla)
            if type(valor) == Exception:
                return valor
            self.tipoDato = Type(self.valor.tipoDato.getTipo())
            return valor
        
        elif self.tipoDato.getTipo() == DataType.VECTOR_ANY or self.tipoDato.getTipo() == DataType.VECTOR_NUMBER or self.tipoDato.getTipo() == DataType.VECTOR_STRING or self.tipoDato.getTipo() == DataType.VECTOR_BOOLEAN:
            self.valor = Recorrer(self.valor, arbol, tabla)
            return self.valor
        
        elif self.tipoDato.getTipo() == DataType.NULL:
            return None
       
