from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbol import Symbol
import copy

class Declaracion(Instruction):
    def __init__(self,id,tipo,valor,linea,columna):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def interpretar(self, arbol, tabla):
        #DECLARACION DE VARIABLES DE TIPO INTERFACE
        if type(self.tipo)==str:
            tablaActual = tabla
            while (tablaActual!=None):
                print(self.tipo)
                busqueda = tablaActual.getSimbolo(self.tipo)
                
                if busqueda!=None:
                    #Se encontró una variable con ese nombre
                    
                    
                    if busqueda.getTipo() == DataType.INTERFACE:
                        
                        if len(self.valor) == len(busqueda.getValor().getParametros()):
                            atributos = copy.deepcopy(busqueda.getValor().getParametros())
                            for atr,valor in self.valor.items():
                                valorAtr = valor.interpretar(arbol,tabla)
                                if type(valorAtr) == Exception:
                                    return valorAtr
                                
                                if atributos.get(atr) ==  valor.tipoDato.getTipo():
                                    atributos[atr] = valorAtr
                                else:
                                    return Exception("Semántico","El valor del atributo <"+atr+"> no concuerda con el tipo asignado",self.linea,self.columna)
                                
                            
                        else:
                            return Exception("Semántico","El número de atributos ingresado no es correcto",self.linea,self.columna)
                        
                        tabla.setValor(self.id,Symbol(self.tipo,self.id,atributos,"variable de tipo interface",tabla.ambito))
                        return
                        #busqueda.setValor(valor)
                
                    else:
                        return Exception("Semántico","El tipo de dato ingresado no corresponde a una interface",self.linea,self.columna)
                    
                tablaActual = tablaActual.getTablaAnterior()

            return Exception("Semántico","No existe una variable o función con el nombre <"+self.id+">",self.linea,self.columna)
          
        

        #DECLARACION DE VARIABLES DE TIPOS NATIVOS
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

            


