import ply.yacc as yacc
import ply.lex as lex
from LexicF2 import tokens, lexer, erroresLexicos

from src.Compiler.Expresions.nativo import Nativo
from src.Compiler.Instructions.imprimir import Imprimir
from src.Compiler.Symbol.type import *
from src.Compiler.Expresions.aritmeticas import *
from src.Compiler.Expresions.logicas import *
from src.Compiler.Expresions.relacionales import *
from src.Compiler.Instructions.declaracion import *
from src.Compiler.Instructions.asignacion import *
from src.Compiler.Instructions.funcion import *
from src.Compiler.Instructions.llamada import *
from src.Compiler.Expresions.returnIns import *
from src.Compiler.Expresions.funcNativas import *
from src.Compiler.Instructions.ifIns import *
from src.Compiler.Instructions.whileIns import *
from src.Compiler.Instructions.forRange import *
from src.Compiler.Instructions.forOf import *
from src.Compiler.Instructions.breakIns import *
from src.Compiler.Instructions.continueIns import *
from src.Compiler.Instructions.interface import *
from src.Compiler.Instructions.asignacionAtributo import *
from src.Compiler.Expresions.atributo import *
from src.Compiler.Expresions.expArray import *
from src.Compiler.Exceptions.exception import *
from src.Compiler.Instructions.asignacionArray import *

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUALACION','DIFERENTE'),
    ('left', 'MAYORIGUAL', 'MENORIGUAL', 'MAYOR', 'MENOR'),
    ('left','SUMA','RESTA'),
    ('left','MULTIPLICACION','DIVISION','MODULO'),
    ('right', 'NOT'),
    ('right', 'POTENCIA'),
    ('left','PARABRE','PARCIERRA'),
    ('left','PTO','OF'),
    #('right', 'UMENOS'),   
 
)

def p_Inicio(t):
    'init : instrucciones'
    t[0] = t[1]

def p_lista_instrucciones(t):
    'instrucciones : instrucciones instruccion puntoycoma'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instruccion(t):
    'instrucciones : instruccion puntoycoma'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instruccion_global(t):
    '''instruccion : imprimir
                | declaracion
                | asignacion
                | funcion
                | llamada
                | if
                | while
                | for
                | break
                | continue
                | retorno
                | struct
                | asignacion_array'''
    t[0] = t[1]
#Las instrucciones pueden venir con o sin punto y coma al final
def p_puntoycoma(t):
    '''puntoycoma : PTOCOMA
                |'''

def p_puntoycoma_erro(t):
    '''puntoycoma : error PTOCOMA
                | error'''
    erroresLexicos.append("Error sintáctico", "Error", 0,0)

#*************************************INSTRUCCIONES**********************************************
def p_imprimir(t):
    'imprimir : CONSOLE PTO LOG PARABRE lista_parametros_l PARCIERRA'
    t[0] = Imprimir(DataType.INDEFINIDO,t[5],t.lineno(1),9)

def p_tipar(t):
    'tipar : DOSPTOS tipo'
    t[0] = t[2]

def p_declaraciones(t):
    'declaracion : LET ID tipar IGUAL expresion'
    t[0] = Declaracion(t[2],t[3],t[5],t.lineno(1),0)

def p_no_tipar(t):
    'tipar :'
    t[0] = None

def p_asignaciones(t):
    'asignacion : ID IGUAL expresion'
    t[0] = Asignacion(t[1],t[3],t.lineno(1),0)

def p_asignacion_atr(t):
    'asignacion : ID PTO ID IGUAL expresion'
    t[0] = AsignacionAtributo(t[1],t[3],t[5],t.lineno(1),0)

def p_funciones(t): 
    'funcion : FUNCTION ID PARABRE lista_parametros PARCIERRA LLAVEABRE instrucciones LLAVECIERRA puntoycoma'
    #'funcion : FUNCTION ID PARABRE lista_parametros PARCIERRA LLAVEABRE lista_instrucciones #LLAVECIERRA retorno puntoycoma'
    print("Declaracion de funcion ",t[2])
    t[0] = Funcion(t[2],t[4],t[7],t.lineno(1),0)

def p_lista_parametros(t):
    'lista_parametros : lista_parametros COMA ID tipar'
    if t[3]!="":
        t[1][t[3]]=t[4]
        #t[1].append(t[3])
    t[0] = t[1]

def p_parametro(t):
    'lista_parametros : ID tipar'
    if t[1]=="":
        t[0] = {}
    else:
        t[0] = {t[1] : t[2]}

def p_parametro_vacio(t):
    'lista_parametros :'
    t[0] = {}

def p_retorno(t):
    '''retorno : RETURN valor_retorno puntoycoma'''
    t[0] = Return(t[2],t.lineno(1),0)

def p_break(t):
    'break : BREAK'
    t[0] = Break(t.lineno(1),0)

def p_continue(t):
    'continue : CONTINUE'
    t[0] = Continue(t.lineno(1),0)
   
def p_valor_retorno(t):
    '''valor_retorno : expresion'''
    t[0] = t[1]

def p_valor_retorno_vacio(t):
    'valor_retorno :'
    t[0]=None

def p_llamada_funcion(t):
    'llamada : ID PARABRE lista_parametros_l PARCIERRA'
    t[0] = Llamada(t[1],t[3],t.lineno(1),0)

def p_asignacion_array(t):
    'asignacion_array : ID dimensiones IGUAL expresion'
    t[0] = AsignacionArray(t[1], t[2], t[4], t.lineno(1), 0)

def p_lista_parametros_l (t):
    'lista_parametros_l : lista_parametros_l COMA expresion'
    if t[3] != "":
        t[1].append(t[3])
    t[0] = t[1]

def p_parametro_l(t):
    'lista_parametros_l : expresion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_parametro_l_vacio(t):
    'lista_parametros_l :'
    t[0] = []



def p_if(t):
    'if : IF PARABRE expresion PARCIERRA LLAVEABRE instrucciones LLAVECIERRA elseif else'
    t[0] = If(t[3],t[6],t[8],t[9],t.lineno(1),0)

def p_elif(t):
    'elif : ELSEIF'

def p_elseif_list(t):
    'elseif : elseif elif PARABRE expresion PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'
    if t[2]!="":
        t[1][t[4]]=t[7]
        #t[1].append(t[3])
    t[0] = t[1]


def p_elseif(t):
    'elseif : elif PARABRE expresion PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'
    
    if t[1]=="":
        t[0] = {}
    else:
        t[0] = {t[3] : t[6]}

def p_elseif_none(t):
    'elseif :'
    t[0] = None

def p_else(t):
    'else : ELSE LLAVEABRE instrucciones LLAVECIERRA'
    t[0] = t[3]

def p_else_none(t):
    'else :'
    t[0] = None

def p_while(t):
    'while : WHILE PARABRE expresion PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'
    t[0] = While(t[3],t[6],t.lineno(1),0)

def p_for(t):
    'for : FOR PARABRE LET ID rango PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'
   
    if t[5][0]=="=":
        #forRange
        #print(t[4])
        #print(t[5][2])
        t[0] = ForRange(t[4],t[5][1],t[5][2],t[5][3],t[8],t.lineno(1),0)
    else:
        t[0] = ForOf(t[4],t[5][0],t[8],t.lineno(1),0)

def p_rango(t):
    '''rango : IGUAL expresion PTOCOMA expresion PTOCOMA ID incremental
        | IN expresion
        | OF expresion'''
    if t[1] == "=":
        t[0] = ["=",t[2],t[4],t[7]]
    elif t[1] == "in":
        t[0] = [t[2]]
    elif t[1] == "of":
        t[0] = [t[2]]


def p_incremental_mas(t):
    '''incremental : SUMA SUMA
                | RESTA RESTA'''
    if t[1] == '+':
        t[0] = '+'
    else:
        t[0] = '-'

def p_dimensiones(t):
    'dimensiones : dimensiones CORABRE expresion CORCIERRA'
    if t[3] != "":
        t[1].append(t[3])
    t[0] = t[1]

def p_dimension(t):
    'dimensiones : CORABRE expresion CORCIERRA'
    if t[2] == "":
        t[0] = []
    else:
        t[0] = [t[2]]

def p_interface(t):
    'struct : INTERFACE ID LLAVEABRE atributos LLAVECIERRA'
    t[0] = Interface(t[2],t[4],t.lineno(1),0)

#**********************************************EXPRESIONES***************************************
def p_expresiones_logicas(t):
    '''expresion : expresion AND expresion
                | expresion OR expresion
                | NOT expresion'''
    if t[2] == '&&':
        t[0] = Logica(t[1], t[3], Logic(LogicType.AND), t.lineno(1), 9)
    elif t[2] == '||':
        t[0] = Logica(t[1], t[3], Logic(LogicType.OR), t.lineno(1), 9)
    elif t[1] == '!':
       t[0] = Logica(t[2], t[2], Logic(LogicType.NOT), t.lineno(1), 9)

def p_expresiones_relacionales(t):
    '''expresion : expresion MAYOR expresion
                | expresion MENOR expresion
                | expresion IGUALACION expresion
                | expresion DIFERENTE expresion
                | expresion MAYORIGUAL expresion
                | expresion MENORIGUAL expresion'''
    if t[2] == '>':
        t[0] = Relacional(t[1], t[3], Relational(RelationalType.MAYOR), t.lineno(1), 9)
    elif t[2] == '<':
        t[0] = Relacional(t[1], t[3], Relational(RelationalType.MENOR), t.lineno(1), 9)
    elif t[2] == '===':
        t[0] = Relacional(t[1], t[3], Relational(RelationalType.IGUAL), t.lineno(1), 9)
    elif t[2] == '!==':
        t[0] = Relacional(t[1], t[3], Relational(RelationalType.DIFERENTE), t.lineno(1), 9)
    elif t[2] == '>=':
        t[0] = Relacional(t[1], t[3], Relational(RelationalType.MAYORIGUAL), t.lineno(1), 9)
    elif t[2] == '<=':
        t[0] = Relacional(t[1], t[3], Relational(RelationalType.MENORIGUAL), t.lineno(1), 9)

def p_expresiones_aritmeticas(t):
    '''expresion : expresion SUMA expresion
                | expresion RESTA expresion
                | expresion MULTIPLICACION expresion
                | expresion DIVISION expresion
                | expresion POTENCIA expresion
                | expresion MODULO expresion
                | PARABRE expresion PARCIERRA'''
    
    if t[2] == '+':
        t[0] = Aritmetica(t[1], t[3], Aritmetic(AritmeticType.SUMA), t.lineno(1), 9)
    elif t[2] == '-':
        
        t[0] = Aritmetica(t[1], t[3], Aritmetic(AritmeticType.RESTA), t.lineno(1), 9)
    elif t[2] == '*':
        t[0] = Aritmetica(t[1], t[3], Aritmetic(AritmeticType.MULTIPLICACION), t.lineno(1), 9)
    elif t[2] == '/':
        t[0] = Aritmetica(t[1], t[3], Aritmetic(AritmeticType.DIVISION), t.lineno(1), 9)
    elif t[2] == '^':
        t[0] = Aritmetica(t[1], t[3], Aritmetic(AritmeticType.POTENCIA), t.lineno(1), 9)
    elif t[2] == '%':
        t[0] = Aritmetica(t[1], t[3], Aritmetic(AritmeticType.MODULO), t.lineno(1), 9)
    elif t[1] == "(" and t[3] == ")":
        t[0] = t[2]

#def p_expresion_unaria(t):
#    'expresion : RESTA expresion %prec UMENOS'
#    t[0] = Aritmetica(t[2],t[2],Aritmetic(AritmeticType.NEGACION),t.lineno(1),0)

def p_expresiones_nativas(t):
    '''expresion : expr_punto nativas PARABRE parametro_nativa PARCIERRA'''
    if t[4] == None:
        t[0] = FuncionNativa(t[1], t[2], None, t.lineno(1), 9)
    else: 
        t[0] = FuncionNativa(t[1], t[2], t[4], t.lineno(1), 9)

def p_nativas(t):
    '''nativas : TOFIXED
                | TOEXPO
                | TOSTRING
                | TOLOWER
                | TOUPPER
                | SPLIT
                | CONCAT'''
    if t[1] == 'toFixed':
        t[0] = Native(NativeFunc.FIXED)
    elif t[1] == 'toExponential':
        t[0] = Native(NativeFunc.EXPO)
    elif t[1] == 'toString':
        t[0] = Native(NativeFunc.STRING)
    elif t[1] == 'toLowerCase':
        t[0] = Native(NativeFunc.LOWER)
    elif t[1] == 'toUpperCase':
        t[0] = Native(NativeFunc.UPPER)
    elif t[1] == 'split':
        t[0] = Native(NativeFunc.SPLIT)
    elif t[1] == 'concat':
        t[0] = Native(NativeFunc.CONCAT)

def p_parametro_nativa(t):
    'parametro_nativa : expresion'
    t[0] = t[1]

def p_parametro_nativa_v(t):
    'parametro_nativa :'
    t[0] = None

def p_entero(t):
    'expresion : ENTERO'
    t[0] = Nativo(Type(DataType.NUMBER), t[1], t.lineno(1), 9)

def p_decimal(t):
    'expresion : DECIMAL'
    t[0] = Nativo(Type(DataType.NUMBER), t[1], t.lineno(1), 9)

def p_cadena(t):
    'expresion : CADENA'
    t[0] = Nativo(Type(DataType.STRING), t[1], t.lineno(1), 9)

def p_booleano(t):
    '''expresion : FALSO
                | VERDADERO'''
    t[0] = Nativo(Type(DataType.BOOLEAN), t[1], t.lineno(1), 9)

def p_identificador(t):
    'expresion : ID'
    t[0] = Nativo(Type(DataType.ID), t[1], t.lineno(1), 9)

def p_interface_expr(t):
    'expresion : LLAVEABRE atributos_valor LLAVECIERRA'
    t[0] = t[2]

def p_atributos_valor(t):
    'atributos_valor : atributos_valor COMA ID DOSPTOS expresion'
    if t[2]!="":
        t[1][t[3]]=t[5]
        #t[1].append(t[3])
    t[0] = t[1]

def p_atributo_valor(t):
    'atributos_valor : ID DOSPTOS expresion'
    if t[1]=="":
        t[0] = {}
    else:
        t[0] = {t[1] : t[3]}

def p_atributos(t):
    'atributos : atributos ID tipar PTOCOMA'
    if t[2]!="":
        t[1][t[2]]=t[3]
        #t[1].append(t[3])
    t[0] = t[1]

def p_atributo(t):
    'atributos : ID tipar PTOCOMA'
    if t[1]=="":
        t[0] = {}
    else:
        t[0] = {t[1] : t[2]}

def p_valor_atributo(t):
    'expresion : expr_punto ID'
    t[0] = Atributo(t[1],t[2],t.lineno(1),0)

def p_expresion_punto(t):
    'expr_punto : expresion PTO'
    t[0] = t[1]

def p_arreglo(t):
    'expresion : CORABRE lista_parametros_l CORCIERRA'
    t[0] = Nativo(Type(DataType.VECTOR_ANY), t[2], t.lineno(1), 0)

def p_exp_arreglo(t):
    'expresion : ID dimensiones'
    t[0] = Array(Nativo(Type(DataType.ID), t[1], t.lineno(1), 0), t[2], t.lineno(1), 0)

def p_null(t):
    'expresion : NULL'
    t[0] = None

def p_tipos(t):
    '''tipo : NUMBER CORABRE CORCIERRA
            | STRING CORABRE CORCIERRA
            | BOOLEAN CORABRE CORCIERRA
            | ANY CORABRE CORCIERRA
            | ID CORABRE CORCIERRA''' #Cuando el tipo es el nombre de un struct
    t[0] = t[1]

def p_tipo_string(t):
    'tipo : STRING'
    t[0] = DataType.STRING

def p_tipo_number(t):
    'tipo : NUMBER'
    t[0] = DataType.NUMBER

def p_tipo_boolean(t):
    'tipo : BOOLEAN'
    t[0] = DataType.BOOLEAN

def p_tipo_any(t):
    'tipo : ANY'
    t[0] = DataType.ANY

def p_tipo_null(t):
    'tipo : NULL'
    t[0] = DataType.NULL

def p_tipo_struct(t):
    'tipo : ID'
    t[0] = t[1]

def p_expresion_llamada(t):
    'expresion : llamada'
    t[0] = t[1]

def p_error(t):
    erroresLexicos.append(Exception("Error sintactico", str(t.value), t.lexer.lineno, 0))
   
def parsear(input):
    global errores
    global parser 
    global entrada
    errores = []
    parser = yacc.yacc()
    entrada = input
    result = parser.parse(input)
    errores = erroresLexicos
    
    return result, errores