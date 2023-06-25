import re
import ply.lex as lex
#from main import entrada
from src.Interpreter.Exceptions.exception import *

erroresLexicos = []

reservedWords = {
    'null'          : 'NULL',
    'any'           : 'ANY',
    'let'           : 'LET',
    'console'       : 'CONSOLE',
    'log'           : 'LOG',
    'interface'     : 'INTERFACE',
    'true'          : 'VERDADERO',
    'false'         : 'FALSO',
    'string'        : 'STRING',
    'number'        : 'NUMBER',
    'boolean'       : 'BOOLEAN',
    'function'      : 'FUNCTION',
    'return'        : 'RETURN',
    'if'            : 'IF',
    'else'          : 'ELSE',
    'while'         : 'WHILE',  
    'for'           : 'FOR',
    'in'            : 'IN',
    'of'            : 'OF',
    'break'         : 'BREAK',
    'continue'      : 'CONTINUE',
    'toFixed'       : 'TOFIXED',
    'toExponential' : 'TOEXPO',
    'toString'      : 'TOSTRING',
    'toLowerCase'   : 'TOLOWER',
    'toUpperCase'   : 'TOUPPER',
    'split'         : 'SPLIT',
    'concat'        : 'CONCAT',
    'typeOf'        : 'TYPEOF',
    'length'        : 'LENGTH',
}

tokens = [
    #SIMBOLOS
    'PTO',
    'DOSPTOS',
    'IGUAL',
    'PTOCOMA',
    'PARABRE',
    'PARCIERRA',
    'LLAVEABRE',
    'LLAVECIERRA',
    'COMA',
    'CORABRE',
    'CORCIERRA',
    #Operaciones aritméticas
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'POTENCIA',
    'MODULO',
    #RELACIONALES
    'MAYORIGUAL',
    'MENORIGUAL',
    'DIFERENTE',
    'IGUALACION',
    'MAYOR',
    'MENOR',
    #LOGICAS
    'AND',
    'OR',
    'NOT',
    #NATIVOS
    'ENTERO',
    'DECIMAL',
    'CADENA',
    #OTROS
    'ID',
    'ELSEIF'
    
]+ list(reservedWords.values())

# TOKENS
t_PTO           = r'\.'
t_DOSPTOS       = r'\:'
t_IGUAL         = r'\='
t_PTOCOMA       = r'\;'
t_PARABRE       = r'\('
t_PARCIERRA     = r'\)'
t_LLAVEABRE     = r'\{'
t_LLAVECIERRA   = r'\}'
t_CORABRE       = r'\['
t_CORCIERRA     = r'\]'
t_SUMA          = r'\+'
t_RESTA         = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION      = r'\/'
t_POTENCIA      = r'\^'
t_MODULO        = r'\%'
t_MAYORIGUAL    = r'>='
t_MENORIGUAL    = r'<='
t_DIFERENTE     = r'!=='
t_IGUALACION    = r'==='
t_MAYOR         = r'\>'
t_MENOR         = r'\<'
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'\!'
t_COMA          = r'\,'


def t_ELSEIF(token):
    r'else if'
    return token

def t_DECIMAL(token):
    r'\d+\.\d+'
    try:
        token.value = float(token.value)
    except ValueError:
        erroresLexicos.append(Exception("Error léxico", "Valor float muy grande %d" + str(token.value), token.lineno, token.lexpos))
        token.value = 0
    return token

def t_ENTERO(token):
    r'\d+'
    try:
        token.value = int(token.value)
    except ValueError:
        erroresLexicos.append(Exception("Error léxico", "Valor int muy grande %d" + str(token.value), token.lineno, token.lexpos))
        token.value = 0
    return token

def t_CADENA(token):
    r'(\".*?\")'
    token.value = token.value[1:-1]
    token.value = token.value.replace('\\t', '\t')
    token.value = token.value.replace('\\n', '\n')
    token.value = token.value.replace('\\"', '\"')
    token.value = token.value.replace("\\'", "\'")
    token.value = token.value.replace('\\\\', '\\')
    return token

def t_IDENTIFICADOR(token):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    token.type = reservedWords.get(token.value, 'ID')
    return token

def t_UNILINEA(token):
    r'\/\/.*\n'
    token.lexer.lineno += 1

def t_MULTILINEA(token):
    r'\/\*(.|\n)*\*\/'
    token.lexer.lineno += token.value.count('\n')

#Nueva Linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = " \t\r"

def t_error(token):
    print(lexer)
    #erroresLexicos.append(Exception("Error léxico", "Caracter inválido: " + str(token.value[0]), token.lineno, encontrar_columna(entrada, token)))
    token.lexer.skip(1)

lexer = lex.lex(reflags = re.IGNORECASE)
