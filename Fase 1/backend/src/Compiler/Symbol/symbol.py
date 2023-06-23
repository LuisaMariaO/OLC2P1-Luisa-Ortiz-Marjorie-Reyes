class Symbol:
    def __init__(self, identificador,tipo,posicion,globalVar,inHeap):
        self.tipo = tipo
        self.identificador = identificador
        self.posicion = posicion
        self.isGlobal = globalVar
        self.inHeap = inHeap
        self.value = None
        self.tipoAux = ''
        self.length = 0
        self.referencia = False
        self.params = None
        

    def getTipo(self):
        return self.tipo
    def getId(self):
        return self.identificador
    def getPos(self):
        return self.posicion
    def getInHeap(self):
        return self.inHeap
    
    def getParams(self):
        return self.params
    
    def setParams(self, params):
        self.params = params
    
    def setTipo(self, tipo):
        self.tipo = tipo
    def setId(self, id):
        self.identificador = id
    def setPos(self, pos):
        self.posicion = pos
    def setInHeap(self, value):
        self.inHeap = value
    
    def setTipoAux(self, tipo):
        self.tipoAux = tipo

    def getTipoAux(self):
        return self.tipoAux

    def setLength(self, length):
        self.length = length
    def getLength(self):
        return self.length

    def setReferencia(self, ref):
        self.referencia = ref
        
    def getReferencia(self):
        return self.referencia
    
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value