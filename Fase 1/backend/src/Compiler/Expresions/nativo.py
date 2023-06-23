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
        #TODO: Retorno para variables y llamadas
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

       
        return Return(str(self.valor),self.tipoDato,False)