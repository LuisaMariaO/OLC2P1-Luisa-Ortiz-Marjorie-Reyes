from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbolTable import *
import copy
from ..Instructions.continueIns import *
from ..Instructions.breakIns import *
from ..Expresions.returnIns import *
from ..Symbol.generador import Generador

class While(Instruction):
    def __init__(self,condicion,instrucciones,linea,columna):
        self.condicion = condicion
        self.instrucciones = instrucciones

        super().__init__(linea,columna,Type(DataType.INDEFINIDO)) 

    def compilar(self, arbol, tabla):
        genAux = Generador()
        generator = genAux.getInstance()
        generator.addComment("Inicia Loop While")
        while True:
            # bandera = False #Nos servira para el break, o el continue
            if self.getTipo():
                
                Lbl0 = generator.newLabel()
                generator.putLabel(Lbl0)
                condicion = self.condicion.compilar(arbol, tabla)
                if isinstance(condicion, Excepcion): 
                    tree.setExcepciones(condicion)
                generator.putLabel(condicion.getTrueLbl())

                table.breakLbl = condicion.getFalseLbl()
                table.continueLbl = Lbl0
                
                for instruccion in self.instrucciones:
                    entorno = Tabla_Simbolo(table)
                    entorno.breakLbl = condicion.getFalseLbl()
                    entorno.continueLbl = Lbl0
                    entorno.returnLbl = table.returnLbl
                    value = instruccion.compilar(tree, entorno)
                    if isinstance(value, Excepcion): 
                        tree.setExcepciones(condicion)
                    if isinstance(value, Break):
                        generator.addGoto(condicion.getFalseLbl())
                    if isinstance(value, Continue):
                        generator.addGoto(Lbl0)
                    if isinstance(value, ReturnE):
                        if entorno.returnLbl != '':
                            if value.getTrueLbl() == '':
                                generator.addComment('Resultado a retornar en la funcion')
                                generator.setStack('P',value.getValor())
                                generator.addGoto(entorno.returnLbl)
                                generator.addComment('Fin del resultado a retornar')
                            else:
                                generator.addComment('Resultado a retornar en la funcion')
                                generator.putLabel(value.getTrueLbl())
                                generator.setStack('P', '1')
                                generator.addGoto(entorno.returnLbl)
                                generator.putLabel(value.getFalseLbl())
                                generator.setStack('P', '0')
                                generator.addGoto(entorno.returnLbl)
                                generator.addComment('Fin del resultado a retornar')
                table.breakLbl = ''
                table.continueLbl = ''

                generator.addGoto(Lbl0)
                generator.putLabel(condicion.getFalseLbl())
                generator.addComment("Finaliza Loop While")
            break