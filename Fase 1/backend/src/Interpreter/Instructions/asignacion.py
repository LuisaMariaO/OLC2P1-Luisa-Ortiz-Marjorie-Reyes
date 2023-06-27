from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
import copy

class Asignacion(Instruction):
    def __init__(self,id,valor,linea,columna):
        self.id = id
        self.valor = valor
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def interpretar(self, arbol, tabla):
        valor = self.valor.interpretar(arbol,tabla)
        if type(valor) == Exception:
            return valor
        #Recorre la tabla de símbolos buscando el identificador
        tablaActual = tabla
        while (tablaActual!=None):
            busqueda = tablaActual.getSimbolo(self.id)
            #Si se encontró una variable con ese nombre, obtiene el valor y el tipo
            if busqueda != None:
                if type(busqueda.getTipo()) == str and type(valor) == dict:
                    if len(valor) == len(busqueda.getValor()):
                        atributos = copy.deepcopy(busqueda.getValor())
                        for id, val in valor.get("valor").items():
                            atributos[id] = val.getValor()
                        self.valor.tipoDato = Type(DataType.INTERFACE)
                #Si el tipo de la variable coincide con el tipo que se quiere asignar
                if busqueda.getTipo() == self.valor.tipoDato.getTipo() or busqueda.getTipo()==DataType.ANY:
                    busqueda.setValor(valor)
                    return
                elif type(busqueda.getTipo()) == str and self.valor.tipoDato.getTipo() == DataType.INTERFACE:
                    busqueda.setValor(atributos)
                else:
                    return Exception("Error semántico","El tipo de dato de la expresión no coincide con el tipo de dato de la variable", self.linea, self.columna)
                
            tablaActual = tablaActual.getTablaAnterior()

        return Exception("Error semántico","No existe una variable o función con el nombre '" + self.id + "'", self.linea, self.columna)