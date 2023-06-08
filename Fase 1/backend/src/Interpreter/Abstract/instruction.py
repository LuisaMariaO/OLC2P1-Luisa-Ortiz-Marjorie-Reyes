from abc import ABC, abstractmethod

class Instruction(ABC):
    def __init__(self,linea,columna,tipo):
        self.linea = linea
        self.columna = columna
        self.tipoDato = tipo

    @abstractmethod
    def interpretar(self,arbol,tabla):
        pass
        