from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbol import Symbol
from ..Abstract.returnF2 import Return
import copy
from ..Abstract.returnF2 import Return
from ..Symbol.generador import Generador

class Declaracion(Instruction):
    def __init__(self,id,tipo,valor,linea,columna):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.find = True
        self.ghost = -1 #Para ocultar el stack
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def compilar(self, arbol, tabla):
        
        genAux = Generador()
        generador = genAux.getInstance()

        generador.addComment("Declaracion de variable")
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
                                    generador.addComment("Error: El valor del atributo "<+atr+"> no concuerda con el tipo asignado")
                                    return Exception("Semántico","El valor del atributo <"+atr+"> no concuerda con el tipo asignado",self.linea,self.columna)
                                
                            
                        else:
                            generador.addComment("Error: Eñ número de atrinutos ingresado no es correcto")
                            return Exception("Semántico","El número de atributos ingresado no es correcto",self.linea,self.columna)
                        
                        tabla.setValor(self.id,Symbol(self.tipo,self.id,atributos,"variable de tipo interface",tabla.ambito))
                        return
                        #busqueda.setValor(valor)
                
                    else:
                        generador.addComment("Error: El tipo de dato ingresado no corresponde a una interface")
                        return Exception("Semántico","El tipo de dato ingresado no corresponde a una interface",self.linea,self.columna)
                    
                tablaActual = tablaActual.getTablaAnterior()

            return Exception("Semántico","No existe una interface con el nombre <"+self.id+">",self.linea,self.columna)
          
        

        #DECLARACION DE VARIABLES DE TIPOS NATIVOS
     
    
       
        
       
        
        value = self.valor.compilar(arbol, tabla)
        if isinstance(value, Exception): return value # Analisis Semantico -> Error
        # Verificacion de tipos
        if self.tipo == self.valor.tipoDato.getTipo():
            #Si el tipo a guardar es un struct o es una interface, inHeap es verdadero pues son tipos de dato que lo utilizan
            inHeap = value.getTipo().getTipo() == DataType.STRING or value.getTipo() == DataType.INTERFACE
            
            simbolo = tabla.setDeclaracion(self.id, value.getTipo().getTipo(), inHeap, self.find)
            if simbolo==None:
                generador.addComment("Error: Ya existe una variable o función con el nombre <"+self.id+">")
                generador.addSpace()
                return Exception("Semántico","Ya existe una variable o función con el nombre <"+self.id+">",self.linea,self.columna)
            

        else:
            generador.addComment('Error: Los tipos no concuerdan')
            generador.addSpace()
            return Exception("Semantico", "Tipo de dato diferente declarado.", self.fila, self.columna)
            
        
        tempPos = simbolo.posicion
        if not simbolo.isGlobal:
            tempPos = generador.addTemp()
            generador.addExpression(tempPos, 'P', simbolo.pos, '+')


        #Valores booleanos
        if value.getTipo().getTipo() == DataType.BOOLEAN:
            tempLbl = generador.newLabel()
            
            generador.putLabel(value.trueLbl)
            generador.setStack(tempPos, "1")
            
            generador.addGoto(tempLbl)

            generador.putLabel(value.falseLbl)
            generador.setStack(tempPos, "0")

            generador.putLabel(tempLbl)
        else:
            generador.setStack(tempPos, value.value)
        
        generador.addComment("Fin de declaracion de variable")
        generador.addSpace()

            

