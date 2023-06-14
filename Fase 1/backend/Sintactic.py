import ply.yacc as yacc
import ply.lex as lex
from Lexic import tokens
from Lexic import lexer, errors

from src.Interpreter.Expresions.nativo import Nativo
from src.Interpreter.Instructions.imprimir import Imprimir
from src.Interpreter.Symbol.type import *
from src.Interpreter.Expresions.aritmeticas import *
from src.Interpreter.Expresions.logicas import *
from src.Interpreter.Expresions.relacionales import *
from src.Interpreter.Instructions.declaracion import *
from src.Interpreter.Instructions.asignacion import *
<<<<<<< HEAD
from src.Interpreter.Instructions.funcion import *
from src.Interpreter.Instructions.llamada import *
from src.Interpreter.Expresions.returnIns import *
=======
from src.Interpreter.Expresions.funcNativas import *
>>>>>>> 1484bc00940c7d2a4ada6299d7f938da30469c43

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
    ('left','PTO'),
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
                | BREAK
                | CONTINUE
                | retorno
                | asignacion_arreglo
                | struct
                | asignacion_atributo'''
    t[0] = t[1]
#Las instrucciones pueden venir con o sin punto y coma al final
def p_puntoycoma(t):
    '''puntoycoma : PTOCOMA
                |'''
#*************************************INSTRUCCIONES**********************************************
def p_imprimir(t):
    'imprimir : CONSOLE PTO LOG PARABRE expresion PARCIERRA'
   
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

def p_funciones(t): 
    'funcion : FUNCTION ID PARABRE lista_parametros PARCIERRA LLAVEABRE instrucciones LLAVECIERRA puntoycoma'
    #'funcion : FUNCTION ID PARABRE lista_parametros PARCIERRA LLAVEABRE lista_instrucciones #LLAVECIERRA retorno puntoycoma'
    print("Declaracion de funcion ",t[2])
    t[0] = Funcion(t[2],t[4],t[7],t.lineno(1),0)


def p_lista_parametros(t):
    'lista_parametros : lista_parametros COMA ID tipar'
    if t[3]!="":
        t[1][t[3]]=t[4]
        t[1].append(t[3])
    t[0] = t[1]



def p_parametro(t):
    'lista_parametros : ID tipar'
    if t[1]=="":
        t[0] = {}
    else:
        t[0] = {t[1] : t[2]}

def p_parametro_vacio(t):
    'lista_parametros :'
    t[0] = []


def p_retorno(t):
    '''retorno : RETURN valor_retorno puntoycoma'''
    t[0] = Return(t[2],t.lineno(1),0)


    
def p_valor_retorno(t):
    '''valor_retorno : expresion'''
    t[0] = t[1]

def p_valor_retorno_vacio(t):
    'valor_retorno :'
    t[0]=None

def p_llamada_funcion(t):
    'llamada : ID PARABRE lista_parametros_l PARCIERRA'
    
    t[0] = Llamada(t[1],t[3],t.lineno(1),0)

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

def p_elseif_list(t):
    'elseif : elseif ELSEIF PARABRE expresion PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'

def p_elseif(t):
    'elseif : ELSEIF PARABRE expresion PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'

def p_elseif_none(t):
    'elseif :'

def p_else(t):
    'else : ELSE LLAVEABRE instrucciones LLAVECIERRA'

def p_else_none(t):
    'else :'

def p_while(t):
    'while : WHILE PARABRE expresion PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'

def p_for(t):
    'for : FOR PARABRE LET ID rango PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'

def p_rango(t):
    'rango : IGUAL expresion PTOCOMA expresion PTOCOMA ID incremental'

def p_in_of(t):
    'rango : in_of expresion'

def p_incremental_mas(t):
    '''incremental : SUMA SUMA
                | RESTA RESTA'''
    
def p_in_of_t(t):
    '''in_of : IN
            | OF'''

def p_asignacion_arreglo(t):
    'asignacion_arreglo : ID dimensiones IGUAL expresion'

def p_dimensiones(t):
    'dimensiones : dimensiones CORABRE expresion CORCIERRA'

def p_dimension(t):
    'dimensiones : CORABRE expresion CORCIERRA'

def p_interface(t):
    'struct : INTERFACE ID LLAVEABRE atributos LLAVECIERRA'

def p_asignacion_atributo(t):
    'asignacion_atributo : ID PTO ID IGUAL expresion'
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

def p_expresiones_nativas(t):
    '''expresion : expresion PTO nativas PARABRE parametro_nativa PARCIERRA'''
    if t[5] == None:
        t[0] = FuncionNativa(t[1], t[3], None, t.lineno(1), 9)
    else: 
        t[0] = FuncionNativa(t[1], t[3], t[5], t.lineno(1), 9)

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

def p_exp_acceso(t):
    'expresion : ID dimensiones'

def p_interface_expr(t):
    'expresion : LLAVEABRE atributos_valor LLAVECIERRA'

def p_atributos_valor(t):
    'atributos_valor : atributos_valor COMA ID DOSPTOS expresion'

def p_atributo_valor(t):
    'atributos_valor : ID DOSPTOS expresion'

def p_atributos(t):
    'atributos : atributos ID tipar PTOCOMA'

def p_atributo(t):
    'atributos : ID tipar PTOCOMA'

def p_valor_atributo(t):
    'expresion : ID PTO ID'

def p_arreglo(t):
    'expresion : CORABRE lista_valores CORCIERRA'    

def p_lista_valores(t):
    'lista_valores : lista_valores COMA expresion'

def p_valor(t):
    'lista_valores : expresion'

def p_valor_none(t):
    'lista_valores :'

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


def p_expresion_llamada(t):
    'expresion : llamada'
    t[0] = Nativo(Type(DataType.LLAMADA),t[1],t.lineno(1),0)

def p_error(t):
    print("Error sintactico '%s'" % t.value)

def parsear(input):
    global errores
    global parser 
    global entrada
    errores = []
    parser = yacc.yacc()
    entrada = input
    lexer.lineno = 1
    result = parser.parse(input)
    return result