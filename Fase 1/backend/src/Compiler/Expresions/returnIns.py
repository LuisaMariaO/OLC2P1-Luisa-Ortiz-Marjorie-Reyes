from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception

class Return(Instruction):
    def __init__(self, valor,linea, columna):
        self.valor = valor
        
        self.trueLbl = ''
        self.falseLbl = ''
        self.valorComp = None
        super().__init__(linea, columna, DataType.INDEFINIDO)

    def compilar(self, arbol, tabla):
        result = self.valor.compilar(arbol, tabla)
        if isinstance(result, Exception): return result
        self.tipoDato = result.getTipo()
        self.valorComp = result.getValue()
        if self.tipoDato == DataType.BOOLEAN:
            self.trueLbl = result.getTrueLbl()
            self.falseLbl = result.getFalseLbl()
            
        return self

    def getValor(self):
        return self.valorComp
    def getTipo(self):
        return self.tipoDato
    def getTrueLbl(self):
        return self.trueLbl
    
    def getFalseLbl(self):
        return self.falseLbl
    
    def setValor(self, valor):
        self.valor = valor
    
    def setTipo(self, tipo):
        self.tipo  = tipo
    
    def setTrueLbl(self, lbl):
        self.trueLbl = lbl
    def setFalseLbl(self, lbl):
        self.falseLbl = lbl