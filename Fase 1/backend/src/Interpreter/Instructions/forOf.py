from ..Abstract.instruction import Instruction
from ..Symbol.type import*
from ..Exceptions.exception import Exception
from ..Symbol.symbolTable import *
from ..Symbol.symbol import *
from ..Instructions.breakIns import *
from ..Instructions.continueIns import *
from ..Expresions.returnIns import *
import copy

class ForOf(Instruction):
    def __init__(self,id,iterativo,instrucciones,linea,columna):
        self.id = id
        self.iterativo = iterativo
        self.instrucciones = instrucciones

        super().__init__(linea,columna,Type(DataType.INDEFINIDO)) 

    def interpretar(self, arbol, tabla):
        #Crea una nueva tabla y obtiene la expresion a iterar
        tablaNueva = SymbolTable(tabla,"For")
        valueIterate = self.iterativo.interpretar(arbol,tabla)
        #Si no se pudo obtener la expresion a iterar
        if type(valueIterate)==Exception: return valueIterate
        #Verifico que sea un string o un vector
        if self.iterativo.tipoDato.getTipo() != DataType.STRING and self.iterativo.tipoDato.getTipo()!=DataType.VECTOR_ANY and self.iterativo.tipoDato.getTipo()!=DataType.VECTOR_BOOLEAN and self.iterativo.tipoDato.getTipo()!=DataType.VECTOR_ID and self.iterativo.tipoDato.getTipo()!=DataType.VECTOR_BOOLEAN and self.iterativo.tipoDato.getTipo()!=DataType.VECTOR_STRING :
            return Exception("Error semántico: ","Solo se pueden iterar vectores y strings",self.linea,self.columna)
        #Agregar el id que se va a crear dentro de esta tabla
        tablaNueva.setValor(self.id,Symbol(DataType.INDEFINIDO,self.id,None,"Variable local for",tablaNueva.ambito,self.linea,self.columna))

        while(len(valueIterate)>0):
            parar=False
            #Se va a ir actualizando el tipo de dato del simbolo de la tabla en cada iteracion
            simbolo = tablaNueva.getSimbolo(self.id)
            simbolo.setValor(valueIterate[0])
            print(type(valueIterate[0]))
            if type(valueIterate[0])==int or type(valueIterate[0])==float:
                simbolo.setTipo(DataType.NUMBER)
            elif type(valueIterate[0])==str:
                simbolo.setTipo(DataType.STRING)
            elif type(valueIterate[0]) == bool:
                simbolo.setTipo(DataType.BOOLEAN)
            elif type(valueIterate[0]) == list:
                simbolo.setTipo(DataType.VECTOR_ANY)
            elif type(valueIterate[0]) == type(None):
                simbolo.setTipo(DataType.NULL)
            elif type(valueIterate[0]) == any:
                simbolo.setTipo(DataType.ANY)
            else:
                return Exception("Error semántico: ", "Tipo de dato no válido", self.linea, self.columna)
            valueIterate = valueIterate[1:]
            #Recorre las instrucciones
            instruccionesLocales = copy.deepcopy(self.instrucciones)
            for instruccion in instruccionesLocales:
                if isinstance(instruccion,Break):
                    parar = True
                    break
                if isinstance(instruccion,Continue):
                    break
                if isinstance(instruccion,Return):
                    arbol.updateErrores(Exception("Error semántico: ","La instrucción return no es propia de la instrucción for",self.linea,self.columna))
                    continue
                result = instruccion.interpretar(arbol,tablaNueva)
                
                if isinstance(result, Return):
                    return result
                
                if type(result)==Exception:
                    arbol.updateErrores(result)
                    parar = True
            if parar:
                break
            