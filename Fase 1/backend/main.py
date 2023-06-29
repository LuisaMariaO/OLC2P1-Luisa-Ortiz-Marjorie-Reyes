from flask import Flask, request
from flask.json import jsonify
from os import system
from flask_cors import CORS
import base64


import Sintactic
import SintacticF2
from src.Interpreter.Symbol.three import Three
from src.Interpreter.Symbol.symbolTable import SymbolTable
from src.Interpreter.Exceptions.exception import Exception
from src.Interpreter.Instructions.funcion import Funcion
from src.Interpreter.Instructions.interface import Interface
#from src.Interpreter.Exceptions.exception import Exception  as Exception1

#Fase 2
from src.Compiler.Symbol.generador import *
from src.Compiler.Symbol.three import Three as ThreeFase2
from src.Compiler.Symbol.symbolTable import SymbolTable as TableFase2
from src.Compiler.Exceptions.exception import Exception as ExceptionFase2

from src.Compiler.Nativas.lowercase import LowerCase
from src.Compiler.Nativas.uppercase import UpperCase
from src.Compiler.Symbol.type import *

app = Flask(__name__)
CORS(app)
entrada = ""

@app.route('/')
def index():
    return "API is working jus fine! uwu"

@app.route('/parse',methods=['POST'])
def parse():

    data = request.json
    
    try:
        instrucciones = Sintactic.parsear(data.get('code'))
       
        ast = Three(instrucciones[0])
        tabla = SymbolTable(None,"Global")
        ast.setTablaGlobal(tabla)
        
        for instr in ast.getInstrucciones():
            result = instr.interpretar(ast,tabla)
            if type(result) == Exception:
                ast.updateErrores(result)
        graficarErrores(ast.getErrores()+instrucciones[1])
        treeGraph = ast.getTree()
        graficarArbol(treeGraph)
        graficarTabla(ast.getTablaGlobal().tablaActual)
       # listToStr = ' '.join([str(elem) for elem in instrucciones])
        return jsonify({'ok':True, 'msg':'Data recibida', 'consola':ast.getConsola()}),200
    except:
        return jsonify({'ok':False, 'msg':'No es posible analizar la entrada', 'consola':'Error en el servidor :('}), 409
    

@app.route('/compile',methods=['POST'])
def compile():

    data = request.json
    entrada = data.get('code')
    genAux = Generador()
    genAux.cleanAll()
    generador =genAux.getInstance()

    
    try:
        instrucciones = SintacticF2.parsear(data.get('code'))
        ast = ThreeFase2(instrucciones[0])
        tabla = TableFase2(None,"Global")
        ast.setTablaGlobal(tabla)
        agregarNativas(ast)
        
        for instr in ast.getInstrucciones():
            result = instr.compilar(ast,tabla)
            if type(result) == ExceptionFase2:
                ast.updateErrores(result)

        graficarErrores(ast.getErrores()+instrucciones[1])
        graficarTablaC3D(ast.tablaGlobal.tablaActual)
        #treeGraph = ast.getTree()
        #graficarArbol(treeGraph)
        #graficarTabla(tabla)
        #listToStr = ' '.join([str(elem) for elem in instrucciones])
        return jsonify({'ok':True, 'msg':'Data recibida', 'consola':generador.getCode()}),200
    except:
        
        return jsonify({'ok':False, 'msg':'No es posible analizar la entrada', 'consola':'Error en el servidor :('}), 409

@app.route('/symbtable',methods=['GET'])
def symbtable():
    try:
        encoded = encodeImage("TablaSimbolos.png")
        return encoded
    except:
        return jsonify({'ok':False, 'msg':'No es posible analizar la entrada', 'consola':'Error en el servidor :('}), 409
    
@app.route('/errortable',methods=['GET'])
def errortable():
    try:
        encoded = encodeImage("TablaErrores.png")
        return encoded
    except:
        return jsonify({'ok':False, 'msg':'No es posible analizar la entrada', 'consola':'Error en el servidor :('}), 409
    
@app.route('/sintacttree',methods=['GET'])
def sintacttree():
    try:
        encoded = encodeImage("AST.png")
        return encoded
    except:
        return jsonify({'ok':False, 'msg':'No es posible analizar la entrada', 'consola':'Error en el servidor :('}), 409

def graficarArbol(graph):
    Archivo = open("AST.dot", "w", encoding="UTF-8")
    Archivo.write(graph)
    Archivo.close()
    system('dot -Tpng AST.dot -o AST.png')

def graficarTabla(tabla):
    Archivo = open("TablaSimbolos.dot", "w", encoding="UTF-8")
    p1 = '''digraph {
            fontname="Arial"
            label = "Tabla de símbolos"
            node[shape=none]
            n1[label=<
            <table BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\" CELLPADDING=\"4\">]
            <tr>
            <td bgcolor=\"#512D38\"> <font color="white">Nombre </font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Tipo</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Ámbito</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Valor</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Rol</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Fila</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Columna</font></td>
            </tr>\n'''
    color = "#FFE9F3"
    for simbolo in tabla:
        p1 += "<tr>\n"
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].getIdentificador()) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].translateTipo()) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].getAmbito()) + '   </td>\n'
        if isinstance(tabla[simbolo].getValor(), Funcion) or isinstance(tabla[simbolo].getValor(), Interface):
            p1 += '<td bgcolor=\"' + color + '\">       </td>\n'
        else:
            p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].getValor()) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].getRol()) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].getFila()) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].getColumna()) + '   </td>\n'
        p1 += "</tr>\n"
        if color == "#FFE9F3":
            color = "#F4BFDB"
        elif color == "#F4BFDB":
            color = "#FFE9F3"

    p1 += '''</table>
    >]
    }'''
    Archivo.write(p1)
    Archivo.close()
    system('dot -Tpng TablaSimbolos.dot -o TablaSimbolos.png')

def graficarErrores(errores):
    Archivo = open("TablaErrores.dot", "w", encoding="UTF-8")
    p1 = '''digraph {
            fontname="Arial"
            label = "Tabla de errores"
            node[shape=none]
            n1[label=<
            <table BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\" CELLPADDING=\"4\">]
            <tr>
            <td bgcolor=\"#342E37\"> <font color="white"> No. </font> </td>
            <td bgcolor=\"#342E37\"> <font color="white"> Descripción </font> </td>
            <td bgcolor=\"#342E37\"> <font color="white"> Linea </font> </td>
            <td bgcolor=\"#342E37\"> <font color="white"> Columna </font> </td>
            <td bgcolor=\"#342E37\"> <font color="white"> Fecha y hora </font> </td>
            </tr>\n'''
    contador = 1
    color = "#BCF4F5"
    for er in errores:
        p1 += '<tr>\n' + '<td bgcolor=\"' + color + '\">' + str(contador) + "</td>\n" +  er.toString(color) +  '</tr>\n'
        contador += 1
        if color == "#BCF4F5":
            color = "#A4CCF4"
        elif color == "#A4CCF4":
            color = "#BCF4F5"
    p1 += '''</table>
    >]
    }'''
    Archivo.write(p1)
    Archivo.close()
    system('dot -Tpng TablaErrores.dot -o TablaErrores.png')

def graficarTablaC3D(tabla):
    Archivo = open("TablaSimbolos.dot", "w", encoding="UTF-8")
    p1 = '''digraph {
            fontname="Arial"
            label = "Tabla de símbolos"
            node[shape=none]
            n1[label=<
            <table BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\" CELLPADDING=\"4\">]
            <tr>
            <td bgcolor=\"#512D38\"> <font color="white"> Id </font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Tipo</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Posicion</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Es global</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Está en heap</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Valor</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Length</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Referencia</font></td>
            <td bgcolor=\"#512D38\"> <font color="white">Parametros</font></td>
            </tr>\n'''
    color = "#FFE9F3"
    for simbolo in tabla:
        p1 += "<tr>\n"
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].identificador) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].translateTipo()) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].posicion) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].isGlobal) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].inHeap) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].value) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].length) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].referencia) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla[simbolo].params) + '   </td>\n'
        p1 += "</tr>\n"
        if color == "#FFE9F3":
            color = "#F4BFDB"
        elif color == "#F4BFDB":
            color = "#FFE9F3"

    p1 += '''</table>
    >]
    }'''
    Archivo.write(p1)
    Archivo.close()
    system('dot -Tpng TablaSimbolos.dot -o TablaSimbolos.png')

def encodeImage(name):
    with open(name, "rb") as dotimg:
        encodedimg = base64.b64encode(dotimg.read())
        return encodedimg
    
def agregarNativas(ast):
    nombre = "uppercase"
    params = {nombre:DataType.STRING}
    inst = []
    upper = UpperCase("uppercase", params, DataType.STRING,inst, -1, -1)
    lower = LowerCase("lowercase",params,DataType.STRING,inst,-1,-1)
    ast.setFunciones('uppercase',upper)
    ast.setFunciones('lowercase',lower)

   
    
if __name__=='__main__':
    app.run(host='localhost',debug=True)