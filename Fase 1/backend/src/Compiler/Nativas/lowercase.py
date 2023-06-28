from ..Instructions.funcion import Funcion

class LowerCase(Funcion):

    def __init__(self, id, params,tipo, inst, fila, colum):
        super().__init__(id, params,tipo, inst, fila, colum)

    def compilar(self, tree, table):
        return