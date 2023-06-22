from .symbol import Symbol


class SymbolTable:
    def __init__(self,tablaAnterior,ambito):
        self.tablaAnterior = tablaAnterior
        self.tablaActual = {}
        self.ambito = ambito 

        self.breakLbl = ''
        self.continueLbl = ''
        self.returnLbl = ''
        self.recTemps = False
        self.size = 0
        if tablaAnterior != None:
            self.size = self.tablaAnterior.size

    def setDeclaracion(self,id,tipo,inHeap,find=True):
        
        if find:
            tablaActual = self.tablaActual
            while tablaActual != None:
                if id in tablaActual:
                   return None #Si se encuentra la variable, retorno None para reportar el error
                else:
                    tablaActual = self.tablaAnterior
            
        
        simbolo = Symbol(id,tipo,self.size,self.tablaAnterior == None, inHeap)
        self.size += 1
        self.tablaActual[id] = simbolo
        return self.tablaActual[id]
   
    def setAsignacion(self,id,tipo,inHeap,find=True):
        #TODO: Probar con la asignación, cambiar el código de ahí también
 
        if find:
            tablaActual = self.tablaActual
            while tablaActual != None:
                if id in tablaActual: #Si encuentro la variable, la actualizo
                    if tipo == tablaActual[id].getTipo():
                        tablaActual[id].setInHeap(inHeap)
                        return tablaActual[id]
                    else:
                        
                        return "Error: No coinciden los tipos"
                else:
                    tablaActual = self.tablaAnterior
        
        return "Error: No se encontró la variable <"+id+">"

    #def setTabla(self, id, tipo, inHeap, find = True):
    #    if find:
    #        tablaActual = self.tablaActual
    #        while tablaActual != None:
    #            if id in tablaActual:
    #                tablaActual[id].setTipo(tipo)
    #                tablaActual[id].setInHeap(inHeap)
    #                return tablaActual[id]
    #            else:
    #                tablaActual = self.tablaAnterior
    #    if id in self.tablaActual: #Si el id ya existe
    #        self.tablaActual[id].setTipo(tipo)
    #        self.tablaActual[id].setInHeap(inHeap)
    #        return self.tablaActual[id]
    #    else:
    #        simbolo = Symbol(id,tipo,self.size,self.tablaAnterior == None, inHeap)
    #        self.size += 1
    #        self.tablaActual[id] = simbolo
    #        return self.tablaActual[id]
        
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
    
    #def setTabla(self,tabla):
    #    self.tablaActual = tabla

    def getTabla(self, ide): 
        tablaActual = self.tablaActual
        while tablaActual != None:
            if ide in tablaActual:
                return tablaActual[ide]
            else:
                tablaActual = self.tablaAnterior
        return None


