class Symbol:
    def __init__(self, tipo, identificador, valor,rol,ambito):
        self.tipo = tipo
        self.identificador = identificador
        self.valor = valor
        self.rol = rol
        self.ambito = ambito
        

    def getTipo(self):
        return self.tipo
    
    def setTipo(self,tipo):
        self.tipo = tipo

    def getIdentificador(self):
        return self.identificador
    
    def setIdentificador(self, identificador):
        self.identificador = identificador

    def getValor(self):
        return self.valor
    
    def setValor(self,valor):
        self.valor = valor