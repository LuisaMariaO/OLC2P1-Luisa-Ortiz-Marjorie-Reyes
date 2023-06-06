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
    'instrucciones : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instruccion(t):
    'instrucciones : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_imprimir(t):
    'instruccion : CONSOLE PTO LOG PARABRE expresion PARCIERRA PTOCOMA'
    print(t[5])
    t[0] = t[5]

def p_declaraciones(t):
    'instruccion : LET ID DOSPTOS tipo IGUAL expresion PTOCOMA'
    print("Declaracion variable ", t[2], t[4], t[6])
    t[0] = t[6]

def p_asignaciones(t):
    'instruccion : LET ID IGUAL expresion PTOCOMA'
    print("Asignación variable ", t[2], t[4])
    t[0] = t[4]

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
    'expresion : INTERFACE ID LLAVEABRE LLAVECIERRA PTOCOMA'    

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
    return parser.parse(input)

def test_lexer(lexer):
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)

entrada = '''/**/ console.log(3*5-4*2); console.log(9>=5); console.log(false||true);
//Variables\n let _hola1_ : string = "Hola1"; let _hola2_ = "hola2";'''
instrucciones = parsear(entrada)
