class Three:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.errores = []
        self.consola = ""
        self.tablaGlobal = None

    def getConsola(self):
        return self.consola
    
    def setConsola(self,value):
        self.consola = value

    def updateConsola(self,value):
        self.consola = self.consola + "> " + str(value) + '\n'

    def getInstrucciones(self):
        return self.instrucciones
    
    def setInstrucciones(self,instrucciones):
        self.instrucciones = instrucciones

    def getErrores(self):
        return self.errores
    
    def setErrores(self,errores):
        self.errores = errores

    def updateErrores(self,error):
        self.errores.append(error)

    def getTablaGlobal(self):
        return self.tablaGlobal
    
    def setTablaGlobal(self,tabla):
        self.tablaGlobal = tabla