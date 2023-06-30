from datetime import datetime
class Exception:
    def __init__(self,tipo,desc,linea,columna):
        self.tipo = tipo
        self.desc = desc
        self.linea = linea
        self.columna = columna

    def toString(self, color):
        now = datetime.now()
        return '<td bgcolor=\"' + color + '\">   ' + self.tipo + ": " + self.desc + '</td> \n <td bgcolor=\"' + color + '\">   ' + str(self.linea) + '</td> \n <td bgcolor=\"' + color + '\">   ' + str(self.columna) + '</td> \n <td bgcolor=\"' + color + '\">' + now.strftime('%d/%m/%Y, %H:%M:%S') + "</td> \n"