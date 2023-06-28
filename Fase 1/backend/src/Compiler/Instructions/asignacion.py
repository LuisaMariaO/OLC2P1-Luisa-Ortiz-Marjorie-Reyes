from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbol import Symbol
from ..Symbol.generador import Generador

class Asignacion(Instruction):
    def __init__(self,id,valor,linea,columna):
        self.id = id
        self.valor = valor
        self.find = True
        self.ghost = -1 #Para ocultar el stack
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def compilar(self, arbol, tabla):
        genAux = Generador()
        generador = genAux.getInstance()

        generador.addComment("Asignacion de variable")
       
        value = self.valor.compilar(arbol, tabla)
        if isinstance(value, Exception): return value # Analisis Semantico -> Error
        # Verificacion de tipos
       
        #Si el tipo a guardar es un struct o es una interface, inHeap es verdadero pues son tipos de dato que lo utilizan
        inHeap = value.getTipo().getTipo() == DataType.STRING or value.getTipo() == DataType.INTERFACE
            
        simbolo = tabla.setAsignacion(self.id, value.getTipo().getTipo(), inHeap, self.find)
        if type(simbolo)==str:
            generador.addComment(simbolo)
            generador.addSpace()
            
            return Exception("Semántico",simbolo,self.linea,self.columna)
            

       
            
        
        tempPos = simbolo.posicion
        if not simbolo.isGlobal:
            tempPos = generador.addTemp()
            generador.addExp(tempPos, 'P', simbolo.posicion, '+')


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
        
        generador.addComment("Fin de asignacion de variable")
        generador.addSpace()