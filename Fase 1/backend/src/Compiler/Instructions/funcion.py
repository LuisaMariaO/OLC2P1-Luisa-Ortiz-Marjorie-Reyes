from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbolTable import SymbolTable
from ..Expresions.returnIns import Return
from ..Symbol.generador import Generador
from typing import List

class Funcion(Instruction):
    def __init__(self,id,parametros,tipo,instrucciones,linea,columna):
        self.id = id
        self.instrucciones = instrucciones
        self.parametros = parametros
        if tipo == None:
            tipo = Type(DataType.INDEFINIDO)
        self.recTemp = True
        super().__init__(linea,columna,Type(tipo))



    def compilar(self, arbol, tabla):
        funcion = arbol.setFunciones(self.id,self)
        if funcion == 'error': return Exception("Semántico","Ya existe la variable o función <"+self.id+">",self.linea,self.columna)

        genAux = Generador()
        generador = genAux.getInstance()
        generador.addComment(f'Compilación de función {self.id}')

        entorno = SymbolTable(tabla,"Funcion "+self.id)
       
        Lblreturn = generador.newLabel()
        entorno.returnLbl = Lblreturn
        entorno.size = 1 #Porque se reserva el espacio para el retorno de valor de la función
       
        if len(self.parametros) > 0:
            for ide,tipo in self.parametros.items():
                #if parametro['tipo'] == 'struct':
                #    simbolo = entorno.setTabla(parametro['id'], parametro['tipo'], True)
                if not isinstance(tipo, List):
                 
                    simbolo = entorno.setDeclaracion(ide, tipo, (tipo == DataType.STRING  or tipo==DataType.INTERFACE))

                    if simbolo == None: return Exception("Semántico","Ya existe una variable o función <"+self.id+">",self.linea,self.columna)
                
            
        
        generador.addBeginFunc(self.id)

        for instruccion in self.instrucciones:
            value = instruccion.compilar(arbol, entorno)
            if isinstance(value, Exception): return ValueError
            if isinstance(value, Return):
                if value.getTrueLbl() == '':
                    generador.addComment('Resultado a retornar en la funcion')
                    generador.setStack('P',value.getValor())
                    generador.addGoto(entorno.returnLbl)
                    generador.addComment('Fin del resultado a retornar')
                    self.tipoDato = value.getTipo()
                else:
                    generador.addComment('Resultado a retornar en la funcion')
                    generador.putLabel(value.getTrueLbl())
                    generador.setStack('P', '1')
                    generador.addGoto(entorno.returnLbl)
                    generador.putLabel(value.getFalseLbl())
                    generador.setStack('P', '0')
                    generador.addGoto(entorno.returnLbl)
                    generador.addComment('Fin del resultado a retornar')

        generador.addGoto(Lblreturn)
        generador.putLabel(Lblreturn)
       
        generador.addComment(f'Fin de la compilacion de la funcion {self.id}')
        generador.addEndFunc()
        generador.addSpace()
        return


    def getParams(self):
        return self.parametros

    def getTipo(self):
        return self.tipoDato
        