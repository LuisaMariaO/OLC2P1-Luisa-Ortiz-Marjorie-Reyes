class SymbolTable:
    def __init__(self,tablaAnterior,ambito):
        self.tablaAnterior = tablaAnterior
        self.tablaActual = {}
        self.ambito = ambito 

    def getSimbolo(self,ide):
        return self.tablaActual.get(ide)
    
    def setValor(self,ide,simbolo):
        self.tablaActual[ide] = simbolo
    
    def getTablaAnterior(self):
        return self.tablaAnterior
    
    def setTablaAnterior(self,tabla):
        self.tablaAnterior = tabla

    def getTabla(self):
        return self.tablaActual
    
    def setTabla(self,tabla):
        self.tablaActual = tabla


