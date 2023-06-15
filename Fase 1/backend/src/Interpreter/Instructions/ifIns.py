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
        super().__init__(linea,columna,Type(DataType.INDEFINIDO)) 

    def interpretar(self, arbol, tabla):
   
        condition = self.condicion.interpretar(arbol,tabla)
       
        if self.condicion.tipoDato.getTipo()!=DataType.BOOLEAN:
            return Exception("Semántico","La condición debe ser una expresión booleana",self.linea,self.columna)
        if type(condition)==Exception: return condition
        if condition:
            tablaNueva = SymbolTable(tabla,"If")
            for instruccion in self.instrucciones:
                result=instruccion.interpretar(arbol,tablaNueva)
                if type(result)==Exception:
                    arbol.updateErrores(result)
        else:
            
            if self.elifIns!=None:
                for cond,ins in self.elifIns.items():
                    condition = cond.interpretar(arbol,tabla)
                    if self.condicion.tipoDato.getTipo()!=DataType.BOOLEAN:
                        return Exception("Semántico","La condición debe ser una expresión booleana",self.linea,self.columna)
                    if type(condition)==Exception: return condition
                    if condition:
                        tablaNueva = SymbolTable(tabla,"Else if")
                        for instruccion in ins:
                            result=instruccion.interpretar(arbol,tablaNueva)
                            if type(result)==Exception:
                                arbol.updateErrores(result)
                        return
                    
            if self.elseIns!=None:
                tablaNueva = SymbolTable(tabla,"Else")
                for instruccion in self.elseIns:
                    result=instruccion.interpretar(arbol,tablaNueva)
                    if type(result)==Exception:
                        arbol.updateErrores(result)

                    
