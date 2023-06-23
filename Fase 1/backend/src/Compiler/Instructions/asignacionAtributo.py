from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbol import Symbol

class AsignacionAtributo(Instruction):
    def __init__(self,id,atributo,valor,linea,columna):
        self.id = id
        self.atributo = atributo
        self.valor = valor
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def interpretar(self, arbol, tabla):
        

        tablaActual = tabla
        variable = None
        valor = None
        while (tablaActual!=None):
        
            variable = tablaActual.getSimbolo(self.id)
           
            if variable!=None:
                #Se encontró una variable con ese nombre
                valor = self.valor.interpretar(arbol,tabla)
                if type(valor) == Exception:
                    return valor
            tablaActual = tablaActual.getTablaAnterior()
        if variable==None:
            return Exception("Semántico","No existe una variable o función con el nombre <"+self.id+">",self.linea,self.columna)
 
        tablaActual = tabla
        while (tablaActual!=None):
           
            tipo = tablaActual.getSimbolo(variable.getTipo()).getValor()
            
            if tipo!=None:
                #Se encontró la interfaz
               
                if tipo.getParametros().get(self.atributo)==self.valor.tipoDato.getTipo():
                    #Asigno el nuevo valor
                    print(variable.getValor())
                    variable.getValor()[self.atributo] = valor
                    
                    return
                else:
                    return Exception("Sintáctico","El tipo de dato del atributo no concuerda con el del nuevo valor",self.linea,self.columna)
            tablaActual = tablaActual.getTablaAnterior()