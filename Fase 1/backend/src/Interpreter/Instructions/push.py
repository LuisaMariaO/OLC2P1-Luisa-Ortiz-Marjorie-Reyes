from enum import Enum
from ..Abstract.instruction import Instruction
from ..Symbol.type import *

class Push(Instruction):
    def __init__(self, id,posicion,valor, linea, columna):
        print("hola")
        self.id = id
        self.posicion = posicion
        self.valor = valor
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))
    
    def interpretar(self, arbol, tabla):
        print("hoal")
        #Recorre la tabla de símbolos buscando el identificador
        tablaActual = tabla
        while (tablaActual != None):
            simbolo = tablaActual.getSimbolo(self.id)
            #Si se encontró una variable con ese nombre
            if simbolo != None:
                exp = simbolo.getValor()
                if self.valor != None:
                    valor = self.valor.interpretar(arbol,tabla)
                    if type(exp) == list and type(valor) == list:
                        if type(valor) == Exception:
                            return valor
                        if len(self.posicion) == 1:
                            exp[int(self.posicion[0].interpretar(arbol, tabla))].append(valor)
                        elif len(self.posicion) == 2:
                            exp[int(self.posicion[0].interpretar(arbol, tabla))][int(self.posicion[1].interpretar(arbol, tabla))].append(valor)
                        elif len(self.posicion) == 3:
                            exp[int(self.posicion[0].interpretar(arbol, tabla))][int(self.posicion[1].interpretar(arbol, tabla))][int(self.posicion[2].interpretar(arbol, tabla))].append(valor)
                        simbolo.setValor(exp)
                        return
            tablaActual = tablaActual.getTablaAnterior()

        return Exception("Error semántico","No existe una variable o función con el nombre '" + self.id + "'", self.linea, self.columna)