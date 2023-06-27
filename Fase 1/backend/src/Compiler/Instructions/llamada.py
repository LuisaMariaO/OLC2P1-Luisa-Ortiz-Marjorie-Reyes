from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbol import Symbol
from ..Symbol.symbolTable import *
import copy
from ..Expresions.returnIns import *
from ..Instructions.breakIns import *
from ..Instructions.continueIns import *
from ..Symbol.generador import Generador
from ..Exceptions.exception import Exception
from ..Abstract.returnF2 import Return as Return2
from ..Expresions.returnIns import Return


class Llamada(Instruction):
    def __init__(self,id,parametros,linea,columna):
        self.id = id
        self.parametros = parametros
        self.trueLbl = ''
        self.falseLbl = ''
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def compilar(self, arbol, tabla):

        genAux = Generador()
        generador = genAux.getInstance()
        funcion = arbol.getFuncion(self.id)
       

        if funcion != None:
            generador.addComment(f'Llamada a la funcion {self.id}')
            paramValues = []
            temps = []
            size = tabla.size

            for parametros in self.parametros:
                if isinstance(parametros, Llamada):
                    self.guardarTemps(generador, tabla, temps)
                    a = parametros.compilar(arbol, tabla)
                    if isinstance(a, Exception): return a
                    paramValues.append(a)
                    self.recuperarTemps(generador, tabla, temps)
                else:
                    value = parametros.compilar(arbol, tabla)
                    if isinstance(value, Exception):
                        return value
                    paramValues.append(value)
                    temps.append(value.getValue())
            
            temp = generador.addTemp()

            generador.addExp(temp,'P',size+1, '+')
            aux = 0
            if len(funcion.getParams()) == len(paramValues):
                for param in paramValues:
                    if list(funcion.parametros.values())[aux] == param.getTipo().getTipo():
                        aux += 1
                        generador.setStack(temp,param.getValue())
                        if aux != len(paramValues):
                            generador.addExp(temp,temp,1,'+')
                    else:
                        generador.addComment(f'Fin de la llamada a la funcion {self.id} por error, consulte la lista de errores')
                        return Exception("Semantico", f"El tipo de dato de los parametros no coincide con la funcion {self.id}", self.linea, self.columna)

            generador.newEnv(size)
            self.getFuncion(generator=generador) # Sirve para llamar a una funcion nativa
            generador.callFun(funcion.id)
            generador.getStack(temp,'P')
            generador.retEnv(size)
            generador.addComment(f'Fin de la llamada a la funcion {self.id}')
            generador.addSpace()
            self.tipoDato = funcion.getTipo()
            if funcion.getTipo() != DataType.BOOLEAN:

                return Return2(temp, funcion.getTipo(), True)
            else:
                generador.addComment('Recuperacion de booleano')
                if self.trueLbl == '':
                    self.trueLbl = generador.newLabel()
                if self.falseLbl == '':
                    self.falseLbl = generador.newLabel()
                generador.addIf(temp,1,'==',self.trueLbl)
                generador.addGoto(self.falseLbl)
                ret = Return(temp, funcion.getTipo(), True)
                ret.trueLbl = self.trueLbl
                ret.falseLbl = self.falseLbl
                generador.addComment('Fin de recuperacion de booleano')
                return ret

    def guardarTemps(self, generador, tabla, tmp2):
        generador.addComment('Guardando temporales')
        tmp = generador.addTemp()
        for tmp1 in tmp2:
            generador.addExp(tmp, 'P', tabla.size, '+')
            generador.setStack(tmp, tmp1)
            tabla.size += 1
        generador.addComment('Fin de guardado de temporales')
    
    def recuperarTemps(self, generador, tabla, tmp2):
        generador.addComment('Recuperando temporales')
        tmp = generador.addTemp()
        for tmp1 in tmp2:
            tabla.size -= 1
            generador.addExp(tmp, 'P', tabla.size, '+')
            generador.getStack(tmp1, tmp)
        generador.addComment('Fin de recuperacion de temporales')

    def getFuncion(self, generator):
        if self.id == 'length':
            generator.fLength()
        elif self.id == 'trunc':
            generator.fTrunc()
        elif self.id == 'float':
            generator.fFloat()
        elif self.id == 'uppercase':
            generator.fUpperCase()
        elif self.id == 'lowercase':
            generator.fLowerCase()
        return
        
        