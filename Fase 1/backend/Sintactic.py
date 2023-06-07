import ply.yacc as yacc
import ply.lex as lex
from Lexic import tokens
from Lexic import lexer, errors

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
                | llamada'''
    t[0] = t[1]
#Las instrucciones pueden venir con o sin punto y coma al final
def p_puntoycoma(t):
    '''puntoycoma : PTOCOMA
                |'''
#*************************************INSTRUCCIONES**********************************************
def p_imprimir(t):
    'imprimir : CONSOLE PTO LOG PARABRE expresion PARCIERRA'
    print(t[5])
    t[0] = t[5]

def p_declaraciones(t):
    'declaracion : LET ID tipar IGUAL expresion'
    print("Declaracion variable ", t[2], t[4], t[6])
    t[0] = t[6]

def p_tipar(t):
    'tipar : DOSPTOS tipo'

def p_no_tipar(t):
    'tipar :'

def p_asignaciones(t):
    'asignacion : ID IGUAL expresion'
    print("Asignación variable ", t[1], t[3])
    t[0] = t[3]

def p_funciones(t): 
    'funcion : FUNCTION ID PARABRE lista_parametros PARCIERRA LLAVEABRE lista_instrucciones retorno LLAVECIERRA puntoycoma'
    #'funcion : FUNCTION ID PARABRE lista_parametros PARCIERRA LLAVEABRE lista_instrucciones #LLAVECIERRA retorno puntoycoma'
    print("Declaracion de funcion ",t[2])
    t[0] = t[2]


def p_lista_parametros(t):
    'lista_parametros : lista_parametros COMA ID tipar'
    if t[3]!="":
        t[1].append(t[3])
    t[0] = t[1]



def p_parametro(t):
    'lista_parametros : ID tipar'
    if t[1]=="":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_parametro_vacio(t):
    'lista_parametros :'
    t[0] = None


def p_lista_instrucciones_f(t):
    'lista_instrucciones : lista_instrucciones instruccion_f puntoycoma'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instruccion_f(t):
    'lista_instrucciones : instruccion_f puntoycoma'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]



def p_instruccion_funcion(t):
    '''instruccion_f : imprimir
                | declaracion
                | asignacion
                | llamada'''
    t[0] = t[1]



def p_retorno(t):
    '''retorno : RETURN valor_retorno puntoycoma'''
    t[0] = t[2]

def p_retorno_vacio(t):
    'retorno :'
    t[0] = None
    

def p_valor_retorno(t):
    '''valor_retorno : expresion'''
    t[0] = t[1]

def p_valor_retorno_vacio(t):
    'valor_retorno :'
    t[0]=None

def p_llamada_funcion(t):
    'llamada : ID PARABRE lista_parametros_l PARCIERRA'

def p_lista_parametros_l (t):
    'lista_parametros_l : lista_parametros_l COMA expresion'

def p_parametro_l(t):
    'lista_parametros_l : expresion'

def p_parametro_l_vacio(t):
    'lista_parametros_l :'
#**********************************************EXPRESIONES***************************************
def p_expresiones_logicas(t):
    '''expresion : expresion AND expresion
                | expresion OR expresion
                | NOT expresion'''
    if t[2] == '&&':
        t[0] = t[1] and t[3]
    elif t[2] == '||':
        t[0] = t[1] or  t[3]
    elif t[1] == '!':
        t[0] = not t[2]

def p_expresiones_relacionales(t):
    '''expresion : expresion MAYOR expresion
                | expresion MENOR expresion
                | expresion IGUALACION expresion
                | expresion DIFERENTE expresion
                | expresion MAYORIGUAL expresion
                | expresion MENORIGUAL expresion
                | expresion POTENCIA expresion
                | expresion MODULO expresion'''
    if t[2] == '>':
        t[0] = t[1] > t[3]
    elif t[2] == '<':
        t[0] = t[1] < t[3]
    elif t[2] == '===':
        t[0] = t[1] == t[3]
    elif t[2] == '!==':
        t[0] = t[1] != t[3]
    elif t[2] == '>=':
        t[0] = t[1] >= t[3]
    elif t[2] == '<=':
        t[0] = t[1] <= t[3]
    elif t[2] == '^':
        t[0] = pow(t[1], t[3])
    elif t[2] == '%':
        t[0] = t[1] % t[3]

def p_expresiones_aritmeticas(t):
    '''expresion : expresion SUMA expresion
                | expresion RESTA expresion
                | expresion MULTIPLICACION expresion
                | expresion DIVISION expresion'''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]

def p_entero(t):
    'expresion : ENTERO'
    t[0] = int(t[1])

def p_decimal(t):
    'expresion : DECIMAL'
    t[0] = float(t[1])    

def p_cadena(t):
    'expresion : CADENA'
    t[0] = t[1]

def p_booleano(t):
    '''expresion : FALSO
                | VERDADERO'''
    if t[1] == 'false':
        t[0] = False
    elif t[1] == 'true':
        t[0] = True

def p_identificador(t):
    'expresion : ID'
    t[0] = t[1]

def p_interface(t):
    'expresion : INTERFACE ID LLAVEABRE LLAVECIERRA'    

def p_null(t):
    'expresion : NULL'
    t[0] = None

def p_tipos(t):
    '''tipo : STRING
            | NUMBER
            | BOOLEAN'''
    t[0] = t[1]

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