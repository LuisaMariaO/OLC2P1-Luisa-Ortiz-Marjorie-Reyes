class Three:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones.get("instruc")
        self.errores = []
        self.consola = ""
        self.tablaGlobal = None
        self.rootNode = instrucciones.get("nodo")
        self.graphIndex = 0
        self.graph = ""

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

    def getRaiz(self):
        return self.rootNode
    
    def construirTree(self, padre, nodoPadre):
        nodos = padre.getHijos()
        for nodo in nodos:
            self.graphIndex += 1
            self.graph += "n" + str(self.graphIndex) + "[label=\"" + str(nodo.getValor()) + "\"];\n"
            node = "n" + str(self.graphIndex)
            self.graph += nodoPadre + "->" + node + "\n"
            self.construirTree(nodo, node)

    def getTree(self):
        self.graph = "digraph G {\n"
        actual = self.rootNode
        node = "n" + str(self.graphIndex)
        self.graph += "n" + str(self.graphIndex) + "[label=\"" + str(actual.getValor()) + "\"];\n"
        self.construirTree(actual, node)
        self.graph += "}"
        return self.graph
    
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []
        self.padre = None

    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor

    def getHijos(self):
        return self.hijos

    def setHijos(self, hijos):
        self.hijos = hijos
    
    def getPadre(self):
        return self.padre

    def setPadre(self, padre):
        self.padre = padre

    def setProduccion(self, labels):
        for label in labels:
            if type(label) == str:
                self.hijos.append(Nodo(label))
            elif isinstance(label, Nodo):
                self.hijos.append(label)
        return self
    
