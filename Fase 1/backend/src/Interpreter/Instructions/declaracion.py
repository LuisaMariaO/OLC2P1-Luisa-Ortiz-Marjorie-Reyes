from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbol import Symbol
import copy

class Declaracion(Instruction):
    def __init__(self,id,tipo,valor,linea,columna):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        super().__init__(linea,columna,Type(DataType.INDEFINIDO))

    def interpretar(self, arbol, tabla):
        valor = self.valor.interpretar(arbol,tabla)
        #DECLARACION DE VARIABLES DE TIPO INTERFACE
        if type(self.tipo)==str:
            tablaActual = tabla
            while (tablaActual != None):
                busqueda = tablaActual.getSimbolo(self.tipo)
                #Si encontró una variable con ese nombre
                if busqueda!=None:
                    if busqueda.getTipo() == DataType.INTERFACE:
                        if len(valor) == len(busqueda.getValor().getParametros()):
                            atributos = copy.deepcopy(busqueda.getValor().getParametros())
                            for atr,val in valor.items():
                                atributos[atr] = val
                        else:
                            return Exception("Error semántico: ","El número de atributos ingresado no es correcto",self.linea,self.columna)

                        tabla.setValor(self.id,Symbol(self.tipo,self.id,atributos,"variable de tipo interface",tabla.ambito,self.linea,self.columna))
                        return
                        #busqueda.setValor(valor)
                
                    else:
                        return Exception("Error semántico: ","El tipo de dato ingresado no corresponde a una interface",self.linea,self.columna)
                    
                tablaActual = tablaActual.getTablaAnterior()

            return Exception("Error semántico: ","No existe una variable o función con el nombre '"+self.id+"'",self.linea,self.columna)
        
        elif type(valor) == dict:
            self.tipo = valor.get("tipo")
            self.valor = valor.get("valor")
            tablaActual = tabla
            while (tablaActual != None):
                busqueda = tablaActual.getSimbolo(self.tipo)
                #Si encontró una variable con ese nombre
                if busqueda!=None:
                    if busqueda.getTipo() == DataType.INTERFACE:
                        if len(self.valor) == len(busqueda.getValor().getParametros()):
                            atributos = copy.deepcopy(busqueda.getValor().getParametros())
                            for atr,valor in self.valor.items():
                                atributos[atr] = valor.getValor()
                        else:
                            return Exception("Error semántico: ","El número de atributos ingresado no es correcto",self.linea,self.columna)
                        tabla.setValor(self.id,Symbol(self.tipo,self.id,atributos,"variable de tipo interface",tabla.ambito,self.linea,self.columna))
                        return
                    else:
                        return Exception("Error semántico: ","El tipo de dato ingresado no corresponde a una interface",self.linea,self.columna)
                    
                tablaActual = tablaActual.getTablaAnterior()
            return Exception("Error semántico: ","No existe una interfaz con el nombre '"+self.id+"'",self.linea,self.columna)
        
        
        #DECLARACION DE VARIABLES SIN VALOR Y SIN TIPO DE DATO
        elif self.valor == None:
            if self.tipo == None:
                self.valor = ""
                self.tipo = DataType.ANY
                tablaActual = tabla
                while (tablaActual!=None):
                    busqueda = tablaActual.getSimbolo(self.id)
                    if busqueda!=None:
                        return Exception("Error semántico","Ya existe una variable o función con ese nombre '"+self.id+"'",self.linea,self.columna)
                    tablaActual = tablaActual.getTablaAnterior()
                valor = self.valor
                tabla.setValor(self.id,Symbol(self.tipo,self.id,valor,"Variable",tabla.ambito,self.linea,self.columna))
            else:
                if self.tipo == DataType.STRING:
                    self.valor = ""
                elif self.tipo == DataType.NUMBER:
                    self.valor = 0.0
                elif self.tipo == DataType.BOOLEAN:
                    self.valor = False
                elif self.tipo == DataType.VECTOR_ANY:
                    self.valor = []
                elif self.tipo == DataType.NULL:
                    self.valor = None
                elif self.tipo == DataType.ANY:
                    self.valor = ""
                else:
                    return Exception("Error semántico: ","Tipo de dato inválido para declarar variable", self.linea, self.columna)
                tablaActual = tabla
                while (tablaActual!=None):
                    busqueda = tablaActual.getSimbolo(self.id)
                    if busqueda!=None:
                        return Exception("Error semántico","Ya existe una variable o función con ese nombre '"+self.id+"'",self.linea,self.columna)
                    tablaActual = tablaActual.getTablaAnterior()
                valor = self.valor
                tabla.setValor(self.id,Symbol(self.tipo,self.id,valor,"Variable",tabla.ambito,self.linea,self.columna))
        #DECLARACION DE VARIABLES DE TIPOS NATIVOS
        #DECLARACION DE VARIABLES DE ARREGLOS
        else: 

            if type(valor) == Exception:
                return
            
            if self.tipo == None:
                if valor==None:
                    self.tipo = DataType.NULL
                elif type(valor) == int or type(valor) == float:
                    self.tipo = DataType.NUMBER
                elif type(valor) == str:
                    self.tipo = DataType.STRING
                elif type(valor) == bool:
                    self.tipo = DataType.BOOLEAN
                elif type(valor) == list:
                    self.tipo = DataType.VECTOR_ANY

            if self.valor.tipoDato.getTipo() != self.tipo and self.tipo!=DataType.ANY:
            #Si el valor de la expresion no coincide con el de la variable, se retorna un error
                return Exception("Semantico","El tipo de dato del valor no coincide con el de la variable",self.linea,self.columna)
            else:
                tablaActual = tabla
                while (tablaActual!=None):
                    busqueda = tablaActual.getSimbolo(self.id)
                    if busqueda!=None:
                        return Exception("Error semántico","Ya existe una variable o función con ese nombre '"+self.id+"'",self.linea,self.columna)
                    tablaActual = tablaActual.getTablaAnterior()
                tabla.setValor(self.id,Symbol(self.tipo,self.id,valor,"Variable",tabla.ambito,self.linea,self.columna))


            


