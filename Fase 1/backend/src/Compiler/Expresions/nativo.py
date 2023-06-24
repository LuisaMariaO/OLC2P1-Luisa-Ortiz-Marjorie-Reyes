from ..Abstract.instruction import Instruction
from ..Symbol.type import *
from ..Abstract.returnF2 import *
from ..Symbol.generador import *
from ..Exceptions.exception import Exception

class Nativo(Instruction):
    def __init__(self,tipo,valor,linea,columna):
        self.valor = valor
        super().__init__(linea,columna,tipo)

    def getValor(self):
        return self.valor
    
    def compilar(self, arbol, tabla):
        genAux = Generador()
        generador = genAux.getInstance()
        #TODO: Retorno para llamadas
        if self.tipoDato.getTipo()==DataType.ID:
            generador.addComment("Compilacion de acceso")
            simbolo = tabla.getTabla(self.valor)
            if simbolo==None:
                generador.addComment("Error: No se encontro la variable <"+self.valor+">")
                generador.addSpace()
                return Exception("Semántico","No se encontró la variable <"+self.valor+">",self.linea,self.columna)
        
            
            #Temporal para la variable
            temp = generador.addTemp()
            temPos = simbolo.posicion
            if not simbolo.isGlobal:
                temPos = generador.addTemp()
                generador.addExp(temPos,'P',simbolo.posicion,'+')

            generador.getStack(temp,temPos)
            generador.addComment("Fin de compilacion de acceso")
            generador.addSpace()

            #ret = Return(None,DataType.BOOLEAN,False)
            #ret.trueLbl = self.trueLbl
            #ret.falseLbl = self.falseLbl
            self.tipoDato = Type(simbolo.tipo)
            return Return(temp,simbolo.tipo,True)

        elif self.tipoDato.getTipo() == DataType.STRING:
            temporal = generador.addTemp()
            generador.addAsignacion(temporal, 'H') #Le mandamos el heap porque en el stack se va a guardar la posición en donde comienza la cadena, la cual estará almacenada en el heap
            for char in str(self.valor):
                generador.setHeap('H',ord(char)) #No se guarda el caracter en sí, se guarda el ascii porque el heap es un arreglo de números float64
                generador.nextHeap() #Aumento el heao en una posición

            generador.setHeap('H',-1) #-1 es el fin de cadena
            generador.nextHeap()

            return Return(temporal,self.tipoDato,True)

            
        elif self.tipoDato.getTipo() == DataType.NUMBER:    
            return Return(str(self.valor),self.tipoDato,False)
        
        elif self.tipoDato.getTipo() == DataType.BOOLEAN:
            pass