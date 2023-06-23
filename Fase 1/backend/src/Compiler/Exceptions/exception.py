class Exception:
    def __init__(self,tipo,desc,linea,columna):
        self.tipo = tipo
        self.desc = desc
        self.linea = linea
        self.columna = columna

    def toString(self):
        return self.tipo + ' - ' + self.desc + ' [' + str(self.linea) + ', ' + str(self.columna) + '];'