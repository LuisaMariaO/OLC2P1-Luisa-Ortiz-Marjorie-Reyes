from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception

class AsignacionArray(Instruction):
    def __init__(self,id,posicion,valor,linea,columna):
        self.id = id
        self.posicion = posicion
        self.valor = valor
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def interpretar(self, arbol, tabla):
        #Recorre la tabla de símbolos buscando el identificador
        tablaActual = tabla
        while (tablaActual != None):
            simbolo = tablaActual.getSimbolo(self.id)
            #Si se encontró una variable con ese nombre
            if simbolo != None:
                exp = simbolo.getValor()
                valor = self.valor.interpretar(arbol,tabla)
                if type(valor) == Exception:
                    return valor
                if len(self.posicion) == 1:
                    exp[int(self.posicion[0].interpretar(arbol, tabla))] = valor
                elif len(self.posicion) == 2:
                    exp[int(self.posicion[0].interpretar(arbol, tabla))][int(self.posicion[1].interpretar(arbol, tabla))] = valor
                elif len(self.posicion) == 3:
                    exp[int(self.posicion[0].interpretar(arbol, tabla))][int(self.posicion[1].interpretar(arbol, tabla))][int(self.posicion[2].interpretar(arbol, tabla))] = valor
                simbolo.setValor(exp)
                return
            tablaActual = tablaActual.getTablaAnterior()

        return Exception("Error semántico","No existe una variable o función con el nombre '" + self.id + "'", self.linea, self.columna)