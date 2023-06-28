from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbolTable import *
from ..Symbol.generador import Generador
from ..Expresions.returnIns import Return

class If(Instruction):
    def __init__(self,condicion,instrucciones,elseIns,elifIns,linea,columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.elifIns = elifIns
        self.elseIns = elseIns
        super().__init__(linea,columna,Type(DataType.INDEFINIDO)) 

    def compilar(self, arbol, tabla):
   
        genAux = Generador()
        generador = genAux.getInstance()
        generador.addComment('Compilacion de un if')
        condicion = self.condicion.compilar(arbol, tabla) # True o False
        if isinstance(condicion, Exception) : return condicion
      
        if condicion.getTipo().getTipo() == DataType.BOOLEAN:
            generador.putLabel(condicion.getTrueLbl())
            entorno = SymbolTable(tabla,"If")  #NUEVO ENTORNO - HIJO - Vacio
            for instruccion in self.instrucciones:
                entorno.breakLbl = tabla.breakLbl
                entorno.continueLbl = tabla.continueLbl
                entorno.returnLbl = tabla.returnLbl
                result = instruccion.compilar(arbol, entorno)
                if isinstance(result, Exception):return result
                # if isinstance(result, Break):
                #     if tabla.breakLbl != '':
                #         generador.addGoto(tabla.breakLbl)
                #     else:
                #         salir = generador.newLabel()
                #         generador.addGoto(salir)
                #         generador.putLabel(result.getLbl())
                #         generador.putLabel(salir)
                #         return Excepcion("Semantico", "Sentencia break fuera de ciclo", self.fila, self.columna)
                if isinstance(result, Return):
                    if entorno.returnLbl != '':
                        generador.addComment('Resultado a retornar en la funcion')
                        if result.getTrueLbl() == '':
                            generador.setStack('P', result.getValor())
                            generador.addGoto(entorno.returnLbl)
                            generador.addComment('Fin del resultado a retornar en la funcion')
                        else:
                            generador.putLabel(result.getTrueLbl())
                            generador.setStack('P', '1')
                            generador.addGoto(entorno.returnLbl)
                            generador.putLabel(result.getFalseLbl())
                            generador.setStack('P', '0')
                            generador.addGoto(entorno.returnLbl)
                        generador.addComment('Fin del resultado a retornar en la funcion')

            salir = generador.newLabel()
            generador.addGoto(salir)
            generador.putLabel(condicion.getFalseLbl())

            if self.elseIns != None:
                entorno = SymbolTable(tabla,"If else")  #NUEVO ENTORNO - HIJO - Vacio
                for instruccion in self.elseIns:
                    entorno.breakLbl = tabla.breakLbl
                    entorno.continueLbl = tabla.continueLbl
                    entorno.returnLbl = tabla.returnLbl
                    result = instruccion.compilar(arbol, entorno)
                    if isinstance(result, Exception): arbol.updateErrores(result)
                    if isinstance(result, Return):
                        generador.addComment('Resultado a retornar en la funcion')
                        if result.getTrueLbl() == '':
                            generador.setStack('P', result.getValor())
                            generador.addGoto(entorno.returnLbl)
                            generador.addComment('Fin del resultado a retornar en la funcion')
                        else:
                            generador.putLabel(result.getTrueLbl())
                            generador.setStack('P', '1')
                            generador.addGoto(entorno.returnLbl)
                            generador.putLabel(result.getFalseLbl())
                            generador.setStack('P', '0')
                            generador.addGoto(entorno.returnLbl)
                        generador.addComment('Fin del resultado a retornar en la funcion')
            elif self.elifIns != None:
                result = self.elifIns.compilar(arbol, tabla)
                if isinstance(result, Exception): return result
            generador.putLabel(salir)
        generador.addComment('Fin de la compilacion de un if')