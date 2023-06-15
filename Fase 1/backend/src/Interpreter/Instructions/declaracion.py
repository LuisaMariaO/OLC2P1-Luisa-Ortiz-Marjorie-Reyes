from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbol import Symbol

class Declaracion(Instruction):
    def __init__(self,id,tipo,valor,linea,columna):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def interpretar(self, arbol, tabla):
       
        valor = self.valor.interpretar(arbol,tabla)
    
        if type(valor) == Exception:
            return
        
        if self.tipo == None:
            if valor==None:
                self.tipo = DataType.NULL
            elif type(valor) == int or type(valor) == float:
                self.tipo = DataType.NUMBER
            elif type(valor) == str:
                self.tipo = DataType.STRING
            elif type(valor) == bool:
                self.tipo = DataType.BOOLEAN
            
       
        if self.valor.tipoDato.getTipo() != self.tipo and self.tipo!=DataType.ANY:
            
           #Si el valor de la expresion no coincide con el de la variable, se retorna un error
            return Exception("Semantico","El tipo de dato del valor no coincide con el de la variable",self.linea,self.columna)
        else:
          
            tablaActual = tabla
            while (tablaActual!=None):
                busqueda = tablaActual.getSimbolo(self.id)
               
                if busqueda!=None:
                   #Se encontró una variable con ese nombre
                   return Exception("Semántico","Ya existe una variable o función con ese nombre",self.linea,self.columna)
                
              
                tablaActual = tablaActual.getTablaAnterior()
             
          
            tabla.setValor(self.id,Symbol(self.tipo,self.id,valor,"Variable",tabla.ambito))

            


