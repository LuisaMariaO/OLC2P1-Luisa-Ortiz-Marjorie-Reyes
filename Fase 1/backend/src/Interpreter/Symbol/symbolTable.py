class SymbolTable:
    def __init__(self,tablaAnterior):
        self.tablaAnterior = tablaAnterior
        self.tablaActual = {}

    def getSimbolo(self,id):
        return self.tablaActual.get(id)
    
    def setValor(self,id,simbolo):
        self.tablaActual[id] = simbolo
    
    def getTablaAnterior(self):
        return self.tablaAnterior
    
    def setTablaAnterior(self,tabla):
        self.tablaAnterior = tabla

    def getTabla(self):
        return self.tablaActual
    
    def setTabla(self,tabla):
        self.tablaActual = tabla


