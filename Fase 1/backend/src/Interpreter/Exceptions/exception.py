from datetime import datetime
class Exception:
    def __init__(self,tipo,desc,linea,columna):
        self.tipo = tipo
        self.desc = desc
        self.linea = linea
        self.columna = columna

    def toString(self):
        now = datetime.now()
        return '<td>' + self.tipo + ": " + self.desc + '</td> \n <td>' + str(self.linea) + '</td> \n <td>' + str(self.columna) + '</td> \n <td>' + now.strftime('%d/%m/%Y, %H:%M:%S') + "</td> \n"