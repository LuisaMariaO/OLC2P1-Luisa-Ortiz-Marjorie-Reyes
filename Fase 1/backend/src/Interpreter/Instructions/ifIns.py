from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbolTable import *

class If(Instruction):
    def __init__(self,condicion,instrucciones,elifIns,elseIns,linea,columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.elifIns = elifIns
        self.elseIns = elseIns
        super().__init__(linea,columna,DataType.INDEFINIDO) #TODO: Hacer en todas estas Type(DataType.indefinido)

    def interpretar(self, arbol, tabla):
   
        condition = self.condicion.interpretar(arbol,tabla)
       
        if self.condicion.tipoDato.getTipo()!=DataType.BOOLEAN:
            return Exception("Semántico","La condición debe ser una expresión booleana",self.linea,self.columna)
        if type(condition)==Exception: return condition
        if condition:
            tablaNueva = SymbolTable(tabla,"If linea "+str(self.linea))
            for instruccion in self.instrucciones:
                instruccion.interpretar(arbol,tablaNueva)
                if type(instruccion)==Exception:
                    return instruccion
        else:
            
            if self.elifIns!=None:
                for cond,ins in self.elifIns.items():
                    condition = cond.interpretar(arbol,tabla)
                    if self.condicion.tipoDato.getTipo()!=DataType.BOOLEAN:
                        return Exception("Semántico","La condición debe ser una expresión booleana",self.linea,self.columna)
                    if type(condition)==Exception: return condition
                    if condition:
                        tablaNueva = SymbolTable(tabla,"Elif")
                        for instruccion in ins:
                            instruccion.interpretar(arbol,tablaNueva)
                            if type(instruccion)==Exception:
                                return instruccion
                        return
                    
            if self.elseIns!=None:
                tablaNueva = SymbolTable(tabla,"Else")
                for instruccion in self.elseIns:
                    instruccion.interpretar(arbol,tablaNueva)
                    if type(instruccion)==Exception:
                        return instruccion

                    
