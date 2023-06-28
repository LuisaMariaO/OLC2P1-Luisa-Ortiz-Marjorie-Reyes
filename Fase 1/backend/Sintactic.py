import ply.yacc as yacc
import ply.lex as lex
from Lexic import tokens, lexer, erroresLexicos
from LexicF2 import erroresLexicos

from src.Interpreter.Expresions.nativo import Nativo
from src.Interpreter.Instructions.imprimir import Imprimir
from src.Interpreter.Symbol.type import *
from src.Interpreter.Expresions.aritmeticas import *
from src.Interpreter.Expresions.logicas import *
from src.Interpreter.Expresions.relacionales import *
from src.Interpreter.Instructions.declaracion import *
from src.Interpreter.Instructions.asignacion import *
from src.Interpreter.Instructions.funcion import *
from src.Interpreter.Instructions.llamada import *
from src.Interpreter.Expresions.returnIns import *
from src.Interpreter.Expresions.funcNativas import *
from src.Interpreter.Instructions.ifIns import *
from src.Interpreter.Instructions.whileIns import *
from src.Interpreter.Instructions.forRange import *
from src.Interpreter.Instructions.forOf import *
from src.Interpreter.Instructions.breakIns import *
from src.Interpreter.Instructions.continueIns import *
from src.Interpreter.Instructions.interface import *
from src.Interpreter.Instructions.asignacionAtributo import *
from src.Interpreter.Expresions.atributo import *
from src.Interpreter.Expresions.expArray import *
from src.Interpreter.Exceptions.exception import *
from src.Interpreter.Instructions.asignacionArray import *
from src.Interpreter.Symbol.three import Nodo
from src.Interpreter.Expresions.interfaz import *

precedence = (
    ('left',  'OR'),
    ('left',  'AND'),
    ('left',  'IGUALACION','DIFERENTE'),
    ('left',  'MAYORIGUAL', 'MENORIGUAL', 'MAYOR', 'MENOR'),
    ('left',  'SUMA','RESTA'),
    ('left',  'MULTIPLICACION','DIVISION','MODULO'),
    ('right', 'NOT'),
    ('right', 'POTENCIA'),
    ('left',  'PARABRE','PARCIERRA'),
    ('left',  'PTO','OF'),
    ('right', 'UMENOS'),   
 
)

def p_Inicio(t):
    'init : instrucciones'
    t[0] = {"instruc" : t[1].get("instruc"),
            "nodo" : Nodo("init").setProduccion([t[1].get("nodo"), "EOF"])}

def p_lista_instrucciones(t):
    'instrucciones : instrucciones instruccion puntoycoma'
    if t[2] != "":
        t[1].get("instruc").append(t[2].get("instruc"))
    if t[3] == ";":
        t[0] = {"instruc" : t[1].get("instruc"),
            "nodo" : Nodo("instrucciones").setProduccion([t[1].get("nodo"), t[2].get("nodo"), ";"])}
    elif t[3] == None:
        t[0] = {"instruc" : t[1].get("instruc"),
            "nodo" : Nodo("instrucciones").setProduccion([t[1].get("nodo"), t[2].get("nodo")])}

def p_instruccion(t):
    'instrucciones : instruccion puntoycoma'
    if t[1] != "":
        if t[2] == ";":
            t[0] = {"instruc" : [t[1].get("instruc")],
                "nodo" : Nodo("instrucciones").setProduccion([t[1].get("nodo"), ";"])}
        elif t[2] == None:
            t[0] = {"instruc" : [t[1].get("instruc")],
                "nodo" : Nodo("instrucciones").setProduccion([t[1].get("nodo")])}

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
    t[0] = {"instruc" : t[1].get("instruc"),
            "nodo" : t[1].get("nodo")}

#Las instrucciones pueden venir con o sin punto y coma al final
def p_conpuntoycoma(t):
    'puntoycoma : PTOCOMA'
    t[0] = ";"

def p_sinpuntoycoma(t):
    'puntoycoma :'
    t[0] = None

#*************************************INSTRUCCIONES**********************************************
def p_imprimir(t):
    'imprimir : CONSOLE PTO LOG PARABRE lista_parametros_l PARCIERRA'
    t[0] = {"instruc" : Imprimir(DataType.INDEFINIDO,t[5].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("imprimir").setProduccion(["console.log", "(", t[5].get("nodo"), ")"])}

def p_tipar(t):
    'tipar : DOSPTOS tipo'
    t[0] = {"instruc" : t[2].get("instruc"),
            "nodo" : Nodo("tipar").setProduccion([":", t[2].get("nodo")])}

def p_declaraciones(t):
    'declaracion : LET ID tipar declarar'
    if t[3].get("instruc") == None:
        if t[4].get("instruc") == None:
            t[0] = {"instruc" : Declaracion(t[2],None,None,t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("declaracion").setProduccion(["let", t[2]])}
        else :
            t[0] = {"instruc" : Declaracion(t[2],None,t[4].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("declaracion").setProduccion(["let", t[2], "=", t[4].get("nodo")])}
    else:
        if t[4].get("instruc") == None:
            t[0] = {"instruc" : Declaracion(t[2],t[3].get("instruc"),None,t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("declaracion").setProduccion(["let", t[2], t[3].get("nodo")])}
        else :
            t[0] = {"instruc" : Declaracion(t[2],t[3].get("instruc"),t[4].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("declaracion").setProduccion(["let", t[2], t[3].get("nodo"), "=", t[4].get("nodo")])}

def p_no_tipar(t):
    'tipar :'
    t[0] = {"instruc" : None,
            "nodo" : Nodo("tipar").setProduccion(["sin tipado"])}
    
def p_declarar_convalor(t):
    'declarar : IGUAL expresion'
    t[0] = {"instruc" : t[2].get("instruc"),
            "nodo" : t[2].get("nodo")}
    
def p_declarar_sinvalor(t):
    'declarar :'
    t[0] = {"instruc" : None,
            "nodo" : Nodo("none")}

def p_asignaciones(t):
    'asignacion : ID IGUAL expresion'
    t[0] = {"instruc" : Asignacion(t[1],t[3].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("asignacion").setProduccion([t[1], "=", t[3].get("nodo")])}

def p_asignacion_atr(t):
    'asignacion : ID PTO ID IGUAL expresion'
    t[0] = {"instruc": AsignacionAtributo(t[1],t[3],t[5].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("asignacion").setProduccion([t[1], ":", t[3], "=", t[5].get("nodo")])}

def p_funciones(t): 
    'funcion : FUNCTION ID PARABRE lista_parametros PARCIERRA tipar LLAVEABRE instrucciones LLAVECIERRA puntoycoma'
    if t[10] == ";":
        t[0] = {"instruc": Funcion(t[2],t[4].get("instruc"),t[8].get("instruc"),t[6].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo": Nodo("funcion").setProduccion(["funcion", t[2], "(", t[4].get("nodo"), ")", "{", t[8].get("nodo"), "}", ";"])}
    elif t[10] == None:
        t[0] = {"instruc": Funcion(t[2],t[4].get("instruc"),t[8].get("instruc"),t[6].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo": Nodo("funcion").setProduccion(["funcion", t[2], "(", t[4].get("nodo"), ")", "{", t[8].get("nodo"), "}"])}

def p_lista_parametros(t):
    'lista_parametros : lista_parametros COMA ID tipar'
    if t[3]!="":
        t[1].get("instruc")[t[3]]=t[4].get("instruc")
        #t[1].append(t[3])
    t[0] = {"instruc" : t[1].get("instruc"),
            "nodo": Nodo("lista parametros").setProduccion([t[1].get("nodo"), ",", t[3], t[4].get("instruc")]) }

def p_parametro(t):
    'lista_parametros : ID tipar'
    if t[1] == "":
        t[0] = {"instruc" : {},
                "nodo" : Nodo("lista parametros").setProduccion([t[2].get("nodo")])}
    else:
        t[0] = {"instruc" : {t[1] : t[2].get("instruc")},
                "nodo" : Nodo("lista parametros").setProduccion([t[1], t[2].get("nodo")])}

def p_parametro_vacio(t):
    'lista_parametros :'
    t[0] = {"instruc": [],
            "nodo" : Nodo("lista parametros").setProduccion(["sin parametros"])}

def p_retorno(t):
    '''retorno : RETURN valor_retorno puntoycoma'''
    if t[3] == ";":
        t[0] = {"instruc" : Return(t[2].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("retorno").setProduccion(["return", t[2].get("nodo"), ";"])}
    elif t[3] == None:
        t[0] = {"instruc" : Return(t[2].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("retorno").setProduccion(["return", t[2].get("nodo")])}

def p_break(t):
    'break : BREAK'
    t[0] = {"instruc" : Break(t.lineno(1),find_column(entrada, t.lexer)),
            "nodo": Nodo("break") }

def p_continue(t):
    'continue : CONTINUE'
    t[0] = {"instruc" : Continue(t.lineno(1),find_column(entrada, t.lexer)),
            "nodo": Nodo("continue") }
   
def p_valor_retorno(t):
    '''valor_retorno : expresion'''
    t[0] = {"instruc" : t[1].get("instruc"),
            "nodo": Nodo("valor retorno").setProduccion([t[1].get("nodo")]) }

def p_valor_retorno_vacio(t):
    'valor_retorno :'
    t[0 ]= {"instruc" : None,
            "nodo" : Nodo("valor retorno").setProduccion(["sin valor"]) }

def p_llamada_funcion(t):
    'llamada : ID PARABRE lista_parametros_l PARCIERRA'
    t[0] = {"instruc" : Llamada(t[1],t[3].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("llamada").setProduccion([t[1], "(", t[3].get("nodo"), ")"])}

def p_asignacion_array(t):
    'asignacion_array : ID dimensiones IGUAL expresion'
    t[0] = {"instruc" : AsignacionArray(t[1], t[2].get("instruc"), t[4].get("instruc"), t.lineno(1), find_column(entrada, t.lexer)),
            "nodo" : Nodo("asignacion array").setProduccion([t[1], t[2].get("nodo"), "=", t[4].get("nodo")])}

def p_lista_parametros_l (t):
    'lista_parametros_l : lista_parametros_l COMA expresion'
    if t[3] != "":
        t[1].get("instruc").append(t[3].get("instruc"))
    t[0] = {"instruc" : t[1].get("instruc"),
            "nodo" : Nodo("lista parametros").setProduccion([t[1].get("nodo"), ",", t[3].get("nodo")])}

def p_parametro_l(t):
    'lista_parametros_l : expresion'
    t[0] = {"instruc" : [t[1].get("instruc")],
            "nodo" : Nodo("lista parametros").setProduccion([t[1].get("nodo")])}

def p_parametro_l_vacio(t):
    'lista_parametros_l :'
    t[0] = {"instruc" : [],
            "nodo" : Nodo("lista parametros").setProduccion(["sin parametros"])}

def p_if(t):
    'if : IF PARABRE expresion PARCIERRA LLAVEABRE instrucciones LLAVECIERRA elseif else'
    t[0] = {"instruc" : If(t[3].get("instruc"),t[6].get("instruc"),t[8].get("instruc"),t[9].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("if").setProduccion(["if", "(", t[3].get("nodo"), ")", "{", t[6].get("nodo"), "}", t[8].get("nodo"), t[9].get("nodo")])}

def p_elif(t):
    'elif : ELSEIF'

def p_elseif_list(t):
    'elseif : elseif elif PARABRE expresion PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'
    if t[2]!="":
        t[1].get("instruc")[t[4].get("instruc")]=t[7].get("instruc")
        #t[1].append(t[3])
    t[0] = {"instruc" : t[1].get("instruc"),
            "nodo" : Nodo("else if").setProduccion([t[1].get("nodo") , "else if", "(", t[4].get("nodo"), ")", "{", t[7].get("nodo"), "}"])}


def p_elseif(t):
    'elseif : elif PARABRE expresion PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'
    if t[1]=="":
        t[0] = {"instruc" : {},
                "nodo" : Nodo("elseif").setProduccion(["none"])}
    else:
        t[0] = {"instruc" : {t[3].get("instruc") : t[6].get("instruc")},
                "nodo" : Nodo("else if").setProduccion(["else if", "(", t[3].get("nodo"), ")", "{", t[6].get("nodo"), "}"])}

def p_elseif_none(t):
    'elseif :'
    t[0] = {"instruc" : None,
            "nodo" : Nodo("else").setProduccion(["none"])}

def p_else(t):
    'else : ELSE LLAVEABRE instrucciones LLAVECIERRA'
    t[0] = {"instruc" : t[3].get("instruc"),
            "nodo" : Nodo("else").setProduccion(["else", "{", t[3].get("nodo"),"}"])}

def p_else_none(t):
    'else :'
    t[0] = {"instruc" : None,
            "nodo" : Nodo("else").setProduccion(["none"])}

def p_while(t):
    'while : WHILE PARABRE expresion PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'
    t[0] = {"instruc" : While(t[3].get("instruc"),t[6].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("while").setProduccion(["while", "(", t[3].get("nodo"), ")", "{", t[6].get("nodo"), "}"])}

def p_for(t):
    'for : FOR PARABRE LET ID rango PARCIERRA LLAVEABRE instrucciones LLAVECIERRA'
    if t[5].get("instruc")[0]=="=":
        t[0] = {"instruc" : ForRange(t[4],t[5].get("instruc")[1],t[5].get("instruc")[2],t[5].get("instruc")[3],t[8].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
                "nodo": Nodo("for").setProduccion(["for", "(", "let", t[4], t[5].get("nodo"), ")", "{", t[8].get("nodo"), "}"])}
    else:
        t[0] = {"instruc" : ForOf(t[4],t[5].get("instruc")[0],t[8].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
                "nodo": Nodo("for").setProduccion(["for", "(", "let", t[4], t[5].get("nodo"), ")", "{", t[8].get("nodo"), "}"])}

def p_rango(t):
    '''rango : IGUAL expresion PTOCOMA expresion PTOCOMA ID incremental
        | IN expresion
        | OF expresion'''
    if t[1] == "=":
        t[0] = {"instruc" : ["=",t[2].get("instruc"),t[4].get("instruc"),t[7]],
                "nodo" : Nodo("rango").setProduccion(["=", t[2].get("nodo"), ";", t[4].get("nodo"), ";", t[6], t[7]+t[7]])}
    elif t[1] == "in":
        t[0] = {"instruc" : [t[2].get("instruc")],
                "nodo" : Nodo("rango").setProduccion(["in", t[2].get("nodo")])}
    elif t[1] == "of":
        t[0] = {"instruc" : [t[2].get("instruc")],
                "nodo" : Nodo("rango").setProduccion(["of", t[2].get("nodo")])}


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
        t[1].get("instruc").append(t[3].get("instruc"))
    t[0] = {"instruc" : t[1].get("instruc"),
            "nodo" : Nodo("dimensiones").setProduccion([t[1].get("nodo"), "[", t[3].get("nodo"), "]"])}

def p_dimension(t):
    'dimensiones : CORABRE expresion CORCIERRA'
    t[0] = {"instruc" : [t[2].get("instruc")],
            "nodo" : Nodo("dimensiones").setProduccion(["[", t[2].get("nodo"), "]"])}

def p_interface(t):
    'struct : INTERFACE ID LLAVEABRE atributos LLAVECIERRA'
    t[0] = {"instruc" : Interface(t[2],t[4].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("struc").setProduccion(["interface", t[2], "{", t[4].get("nodo"), "}"])}

#**********************************************EXPRESIONES***************************************
def p_expresiones_logicas(t):
    '''expresion : expresion AND expresion
                | expresion OR expresion
                | NOT expresion'''
    if t[2] == '&&':
        t[0] = {"instruc": Logica(t[1].get("instruc"), t[3].get("instruc"), Logic(LogicType.AND), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "&&", t[3].get("nodo")])}
    elif t[2] == '||':
        t[0] = {"instruc": Logica(t[1].get("instruc"), t[3].get("instruc"), Logic(LogicType.OR), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "||", t[3].get("nodo")])}
    elif t[1] == '!':
       t[0] = {"instruc": Logica(t[2].get("instruc"), t[2].get("instruc"), Logic(LogicType.NOT), t.lineno(1), find_column(entrada, t.lexer)),
               "nodo" : Nodo("expresion").setProduccion(["!", t[2].get("nodo")])}

def p_expresiones_relacionales(t):
    '''expresion : expresion MAYOR expresion
                | expresion MENOR expresion
                | expresion IGUALACION expresion
                | expresion DIFERENTE expresion
                | expresion MAYORIGUAL expresion
                | expresion MENORIGUAL expresion'''
    if t[2] == '>':
        t[0] = {"instruc": Relacional(t[1].get("instruc"), t[3].get("instruc"), Relational(RelationalType.MAYOR), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), ">", t[3].get("nodo")])}
    elif t[2] == '<':
        t[0] = {"instruc": Relacional(t[1].get("instruc"), t[3].get("instruc"), Relational(RelationalType.MENOR), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "<", t[3].get("nodo")])}
    elif t[2] == '===':
        t[0] = {"instruc": Relacional(t[1].get("instruc"), t[3].get("instruc"), Relational(RelationalType.IGUAL), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "===", t[3].get("nodo")])}
    elif t[2] == '!==':
        t[0] = {"instruc": Relacional(t[1].get("instruc"), t[3].get("instruc"), Relational(RelationalType.DIFERENTE), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "!==", t[3].get("nodo")])}
    elif t[2] == '>=':
        t[0] = {"instruc": Relacional(t[1].get("instruc"), t[3].get("instruc"), Relational(RelationalType.MAYORIGUAL), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), ">=", t[3].get("nodo")])}
    elif t[2] == '<=':
        t[0] = {"instruc": Relacional(t[1].get("instruc"), t[3].get("instruc"), Relational(RelationalType.MENORIGUAL), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "<=", t[3].get("nodo")])}

def p_expresiones_aritmeticas(t):
    '''expresion : expresion SUMA expresion
                | expresion RESTA expresion
                | expresion MULTIPLICACION expresion
                | expresion DIVISION expresion
                | expresion POTENCIA expresion
                | expresion MODULO expresion
                | PARABRE expresion PARCIERRA'''
    
    if t[2] == '+':
        t[0] = {"instruc": Aritmetica(t[1].get("instruc"), t[3].get("instruc"), Aritmetic(AritmeticType.SUMA), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "+", t[3].get("nodo")])}
    elif t[2] == '-':
        t[0] = {"instruc": Aritmetica(t[1].get("instruc"), t[3].get("instruc"), Aritmetic(AritmeticType.RESTA), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "-", t[3].get("nodo")])}
    elif t[2] == '*':
        t[0] = {"instruc": Aritmetica(t[1].get("instruc"), t[3].get("instruc"), Aritmetic(AritmeticType.MULTIPLICACION), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "*", t[3].get("nodo")])}
    elif t[2] == '/':
        t[0] = {"instruc": Aritmetica(t[1].get("instruc"), t[3].get("instruc"), Aritmetic(AritmeticType.DIVISION), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "/", t[3].get("nodo")])}
    elif t[2] == '^':
        t[0] = {"instruc": Aritmetica(t[1].get("instruc"), t[3].get("instruc"), Aritmetic(AritmeticType.POTENCIA), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "^", t[3].get("nodo")])}
    elif t[2] == '%':
        t[0] = {"instruc": Aritmetica(t[1].get("instruc"), t[3].get("instruc"), Aritmetic(AritmeticType.MODULO), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "%", t[3].get("nodo")])}
    elif t[1] == "(" and t[3] == ")":
        t[0] = {"instruc" : t[2].get("instruc"),
                "nodo" : Nodo("expresion").setProduccion(["(", t[2].get("nodo"), ")"])}

def p_expresion_unaria(t):
    'expresion : RESTA expresion %prec UMENOS'
    t[0] = {"instruc" : Aritmetica(t[2].get("instruc"),t[2].get("instruc"),Aritmetic(AritmeticType.NEGACION),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("expresion").setProduccion(["-", t[2].get("nodo")])}

def p_expresiones_nativas(t):
    '''expresion : expr_punto nativas PARABRE parametro_nativa PARCIERRA'''
    if t[4].get("instruc") == None:
        t[0] = {"instruc" : FuncionNativa(t[1].get("instruc"), t[2].get("instruc"), None, t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), t[2].get("nodo"), "(", ")"])}
    else: 
        t[0] = {"instruc" : FuncionNativa(t[1].get("instruc"), t[2].get("instruc"), t[4].get("instruc"), t.lineno(1), find_column(entrada, t.lexer)),
                "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), t[2].get("nodo"), "(", t[4].get("nodo"), ")"])}

def p_nativas(t):
    '''nativas : TOFIXED
                | TOEXPO
                | TOSTRING
                | TOLOWER
                | TOUPPER
                | SPLIT
                | CONCAT
                | TYPEOF
                | LENGTH'''
    if t[1] == 'toFixed':
        t[0] = {"instruc" : Native(NativeFunc.FIXED),
                "nodo" : Nodo("funcion nativa").setProduccion(["toFixed"])}
    elif t[1] == 'toExponential':
        t[0] = {"instruc" : Native(NativeFunc.EXPO),
                "nodo" : Nodo("funcion nativa").setProduccion(["toExponential"])}
    elif t[1] == 'toString':
        t[0] = {"instruc" : Native(NativeFunc.STRING),
                "nodo" : Nodo("funcion nativa").setProduccion(["toString"])}
    elif t[1] == 'toLowerCase':
        t[0] = {"instruc" :  Native(NativeFunc.LOWER),
                "nodo" : Nodo("funcion nativa").setProduccion(["toLowerCase"])}
    elif t[1] == 'toUpperCase':
        t[0] = {"instruc" : Native(NativeFunc.UPPER),
                "nodo" : Nodo("funcion nativa").setProduccion(["toUpperCase"])}
    elif t[1] == 'split':
        t[0] = {"instruc" : Native(NativeFunc.SPLIT),
                "nodo" : Nodo("funcion nativa").setProduccion(["split"])}
    elif t[1] == 'concat':
        t[0] = {"instruc" : Native(NativeFunc.CONCAT),
                "nodo" : Nodo("funcion nativa").setProduccion(["concat"])}
    elif t[1] == 'typeOf':
        t[0] = {"instruc" : Native(NativeFunc.TYPEOF),
                "nodo" : Nodo("funcion nativa").setProduccion(["typeOf"])}
    elif t[1] == 'length':
        t[0] = {"instruc" : Native(NativeFunc.LENGTH),
                "nodo" : Nodo("funcion nativa").setProduccion(["length"])}

def p_parametro_nativa(t):
    'parametro_nativa : expresion'
    t[0] = {"instruc" : t[1].get("instruc"),
            "nodo" : Nodo("parametro nativa").setProduccion([t[1].get("nodo")])}

def p_parametro_nativa_v(t):
    'parametro_nativa :'
    t[0] = {"instruc" : None,
            "nodo" : Nodo("parametro nativa").setProduccion(["none"])}

def p_entero(t):
    'expresion : ENTERO'
    t[0] = {"instruc" : Nativo(Type(DataType.NUMBER), t[1], t.lineno(1), find_column(entrada, t.lexer)),
            "nodo" : Nodo(str(t[1]))}

def p_decimal(t):
    'expresion : DECIMAL'
    t[0] = {"instruc" : Nativo(Type(DataType.NUMBER), t[1], t.lineno(1), find_column(entrada, t.lexer)),
            "nodo" : Nodo(str(t[1]))}

def p_cadena(t):
    'expresion : CADENA'
    t[0] = {"instruc" : Nativo(Type(DataType.STRING), t[1], t.lineno(1), find_column(entrada, t.lexer)),
            "nodo" : Nodo(str(t[1]))}

def p_booleano(t):
    '''expresion : FALSO
                | VERDADERO'''
    t[0] = {"instruc" : Nativo(Type(DataType.BOOLEAN), t[1], t.lineno(1), find_column(entrada, t.lexer)),
            "nodo" : Nodo(str(t[1]))}

def p_identificador(t):
    'expresion : ID'
    t[0] = {"instruc" : Nativo(Type(DataType.ID), t[1], t.lineno(1), find_column(entrada, t.lexer)),
            "nodo" : Nodo(str(t[1]))}

def p_interface_expr(t):
    'expresion : LLAVEABRE atributos_valor LLAVECIERRA'
    t[0] = {"instruc" : Interfaz(t[2].get("instruc"),t.lineno(1), find_column(entrada, t.lexer)),
            "nodo" : Nodo("expresion").setProduccion(["{", t[2].get("nodo"), "}"])}

def p_atributos_valor(t):
    'atributos_valor : atributos_valor COMA ID ptoexp'
    if t[2]!="":
        t[1].get("instruc")[t[3]]=t[4].get("instruc")
    t[0] = {"instruc" : t[1].get("instruc"),
            "nodo" : Nodo("valor atributos").setProduccion([t[1].get("nodo"), ",", t[3], ":", t[4].get("nodo")])}

def p_atributo_valor(t):
    'atributos_valor : ID ptoexp'
    if t[1]=="":
        t[0] = {"instruc" : {},
                "nodo" : Nodo("valor atributos").setProduccion(["sin valor"])}
    else:
        t[0] = {"instruc" : {t[1] : t[2].get("instruc")},
                "nodo" : Nodo("valor atributos").setProduccion([t[1], ":", t[2].get("nodo")])}

def p_exp_atributo(t):
    'ptoexp : DOSPTOS expresion'
    t[0] = {"instruc" : t[2].get("instruc"),
            "nodo" : Nodo("tipo").setProduccion([t[2].get("nodo")])}

def p_noexp_atributo(t):
    'ptoexp :'
    t[0] = {"instruc" : DataType.ANY,
            "nodo" : Nodo("valor").setProduccion(["sin valor"])}

def p_atributos(t):
    'atributos : atributos ID tipar PTOCOMA'
    if t[2]!="":
        t[1].get("instruc")[t[2]]=t[3].get("instruc")
        #t[1].append(t[3])
    t[0] = {"instruc" : t[1].get("instruc"),
            "nodo" : Nodo("atributos").setProduccion([t[1].get("nodo"), t[2], t[3].get("nodo"), ";"])}

def p_atributo(t):
    'atributos : ID tipar PTOCOMA'
    if t[1]=="":
        t[0] = {"instruc" : {},
                "nodo" : Nodo("atributos").setProduccion(["no hay atributos"])}
    else:
        t[0] = {"instruc" : {t[1] : t[2].get("instruc")},
                "nodo" : Nodo("atributos").setProduccion([t[1], t[2].get("nodo"), ";"])}

def p_valor_atributo(t):
    'expresion : expr_punto ID'
    t[0] = {"instruc" : Atributo(t[1].get("instruc"),t[2],t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), t[2]])}

def p_expresion_punto(t):
    'expr_punto : expresion PTO'
    t[0] = {"instruc" : t[1].get("instruc"),
            "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo"), "."])}

def p_arreglo(t):
    'expresion : CORABRE lista_parametros_l CORCIERRA'
    t[0] = {"instruc" : Nativo(Type(DataType.VECTOR_ANY), t[2].get("instruc"), t.lineno(1), find_column(entrada, t.lexer)),
            "nodo" : Nodo("expresion").setProduccion(["[", t[2].get("nodo"), "]"])}

def p_exp_arreglo(t):
    'expresion : ID dimensiones'
    t[0] = {"instruc" : Array(Nativo(Type(DataType.ID), t[1], t.lineno(1), find_column(entrada, t.lexer)), t[2].get("instruc"), t.lineno(1), find_column(entrada, t.lexer)),
            "nodo" : Nodo("expresion").setProduccion([t[1], t[2].get("nodo")])}

def p_null(t):
    'expresion : NULL'
    t[0] = {"instruc" : Nativo(Type(DataType.NULL), t[1], t.lineno(1), find_column(entrada, t.lexer)),
            "nodo" : Nodo(str(t[1]))}

def p_tipos(t):
    '''tipo : NUMBER CORABRE CORCIERRA
            | STRING CORABRE CORCIERRA
            | BOOLEAN CORABRE CORCIERRA
            | ANY CORABRE CORCIERRA
            | ID CORABRE CORCIERRA
            | NUMBER CORABRE CORCIERRA CORABRE CORCIERRA
            | STRING CORABRE CORCIERRA CORABRE CORCIERRA
            | BOOLEAN CORABRE CORCIERRA CORABRE CORCIERRA
            | ANY CORABRE CORCIERRA CORABRE CORCIERRA
            | ID CORABRE CORCIERRA CORABRE CORCIERRA''' #Cuando el tipo es el nombre de un struct
    t[0] = {"instruc": t[1],
            "nodo" : Nodo("tipo").setProduccion([t[1], "[", "]"])}

def p_tipo_string(t):
    'tipo : STRING'
    t[0] = {"instruc" : DataType.STRING,
            "nodo" : Nodo("tipo").setProduccion(["string"])}

def p_tipo_number(t):
    'tipo : NUMBER'
    t[0] = {"instruc" : DataType.NUMBER,
            "nodo" : Nodo("tipo").setProduccion(["number"])}

def p_tipo_boolean(t):
    'tipo : BOOLEAN'
    t[0] = {"instruc" : DataType.BOOLEAN,
            "nodo" : Nodo("tipo").setProduccion(["boolean"])}

def p_tipo_any(t):
    'tipo : ANY'
    t[0] = {"instruc" : DataType.ANY,
            "nodo" : Nodo("tipo").setProduccion(["any"])}

def p_tipo_null(t):
    'tipo : NULL'
    t[0] = {"instruc" : DataType.NULL,
            "nodo" : Nodo("tipo").setProduccion(["null"])}

def p_tipo_struct(t):
    'tipo : ID'
    t[0] = {"instruc" : t[1],
            "nodo" : Nodo("tipo").setProduccion([t[1]])}

def p_expresion_llamada(t):
    'expresion : llamada'
    t[0] = {"instruc" : Nativo(Type(DataType.LLAMADA),t[1].get("instruc"),t.lineno(1),find_column(entrada, t.lexer)),
            "nodo" : Nodo("expresion").setProduccion([t[1].get("nodo")])}

def p_error(t):
    if t:
        parser.errok()
        erroresLexicos.append(Exception("Error sintáctico: ", t.type, t.lineno, find_column(entrada, t)))
    else:
        erroresLexicos.append(Exception("Error sintáctico en: ", "EOF", t.lineno, t.lexpos ))

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

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