from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbolTable import *
from ..Symbol.symbol import *
from ..Instructions.breakIns import *
from ..Instructions.continueIns import *
from ..Expresions.returnIns import *
from ..Instructions.declaracion import Declaracion
import copy
from ..Symbol.generador import Generador
from ..Expresions.nativo import Nativo
from ..Expresions.aritmeticas import *

class ForRange(Instruction):
    def __init__(self,id,valorDeclaracion,condicion,incremental,instrucciones,linea,columna):
        self.id = id
        self.valorDeclaracion = valorDeclaracion 
        self.condicion = condicion
        self.incremental = incremental
        self.instrucciones = instrucciones
        self.inicio = None

        super().__init__(linea,columna,Type(DataType.INDEFINIDO)) 

    def compilar(self, arbol, tabla):
        genAux = Generador()
        generador = genAux.getInstance()
        generador.addComment('Compilacion de un for')

        bandera = True
        entorno = tabla
        if tabla.getSimbolo(self.id):
            bandera = False

     
        nuevaTabla = SymbolTable(tabla,"For")  # NUEVO ENTORNO
        self.inicio = Declaracion(self.id,DataType.NUMBER,self.valorDeclaracion,self.linea,self.columna)
        inicio = self.inicio.compilar(arbol, nuevaTabla)
        if isinstance(inicio, Exception): return inicio
       
        condicion = self.condicion.compilar(arbol, nuevaTabla)
       
        if isinstance(condicion, Exception): return condicion
        # Validar que el tipo sea booleano
        if self.condicion.tipoDato.getTipo() != DataType.BOOLEAN:
            return Exception("Semantico", "Tipo de dato no booleano en FOR.", self.linea, self.columna)
        # Recorriendo las instrucciones
        while condicion:
            for instruccion in self.instrucciones:
                result = instruccion.compilar(arbol, nuevaTabla)
                if isinstance(result, Exception):arbol.updateErrores(result)
            
            if self.incremental == '+':
                incrementable = Nativo(Type(DataType.NUMBER),1,self.linea,self.columna)
                
                self.aumento = Aritmetica(Nativo(Type(DataType.ID),self.id,self.linea,self.columna),incrementable,Aritmetic(AritmeticType.SUMA),self.linea,self.columna)
            else:
                incrementable = Nativo(Type(DataType.NUMBER),1,self.linea,self.columna)
                self.aumento = Aritmetica(Nativo(Type(DataType.ID),self.id,self.linea,self.columna),incrementable,Aritmetic(AritmeticType.RESTA),self.linea,self.columna)
            nuevo_valor = self.aumento.compilar(arbol, nuevaTabla)
            if isinstance(nuevo_valor, Exception): return nuevo_valor
            
            simbolo = Symbol(self.id, self.inicio.tipo, nuevo_valor, self.linea, self.columna)

            # Actualizando el valor de la variable en la tabla de simbolos
            valor = nuevaTabla.updateTabla(simbolo)

            if isinstance(valor, Exception): return valor

            condicion = self.condicion.compilar(arbol, nuevaTabla)
            if isinstance(condicion, Exception): return condicion
            if self.condicion.tipoDato.getTipo() != DataType.BOOLEAN:
                return Exception("Semantico", "Tipo de dato no booleano en FOR.", self.linea, self.columna)
        return None
            
       