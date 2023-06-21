from abc import ABC, abstractmethod

class Instruction(ABC):
    def __init__(self,linea,columna,tipo):
        self.linea = linea
        self.columna = columna
        self.tipoDato = tipo

        self.trueLbl = ""
        self.falseLbl = ""

    @abstractmethod
    def compilar(self,arbol,tabla):
        pass

    def getTrueLbl(self):
        return self.trueLbl

    def setTrueLbl(self,trueLbl):
        self.trueLbl = trueLbl
    
    def getFalseLbl(self):
        return self.falseLbl
    
    def setFalseLbl(self,falseLbl):
        self.falseLbl = falseLbl
    