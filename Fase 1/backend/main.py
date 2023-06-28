from flask import Flask, request
from flask.json import jsonify
from os import system
from flask_cors import CORS

import Sintactic
import SintacticF2
from src.Interpreter.Symbol.three import Three
from src.Interpreter.Symbol.symbolTable import SymbolTable
from src.Interpreter.Exceptions.exception import Exception as Exception1
from src.Interpreter.Instructions.funcion import Funcion
#from src.Interpreter.Exceptions.exception import Exception  as Exception1

#Fase 2
from src.Compiler.Symbol.generador import *
from src.Compiler.Symbol.three import Three as ThreeFase2
from src.Compiler.Symbol.symbolTable import SymbolTable as TableFase2
from src.Compiler.Exceptions.exception import Exception as ExceptionFase2

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
        graficarTabla(ast.getTablaGlobal())
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
        ast.setTablaGlobal = tabla
        
        
        for instr in ast.getInstrucciones():
            result = instr.compilar(ast,tabla)
            if type(result) == ExceptionFase2:
                ast.updateErrores(result)
        #graficarErrores(ast.getErrores()+instrucciones[1])
        #treeGraph = ast.getTree()
        #graficarArbol(treeGraph)
        #graficarTabla(tabla)
        #listToStr = ' '.join([str(elem) for elem in instrucciones])
        return jsonify({'ok':True, 'msg':'Data recibida', 'consola':generador.getCode()}),200
    except Exception as e:
        print(e)
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
    for simbolo in tabla.tablaActual:
        p1 += "<tr>\n"
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla.tablaActual[simbolo].getIdentificador()) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla.tablaActual[simbolo].translateTipo()) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla.tablaActual[simbolo].getAmbito()) + '   </td>\n'
        if isinstance(tabla.tablaActual[simbolo].getValor(), Funcion):
            p1 += '<td bgcolor=\"' + color + '\">       </td>\n'
        else:
            p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla.tablaActual[simbolo].getValor()) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla.tablaActual[simbolo].getRol()) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla.tablaActual[simbolo].getFila()) + '   </td>\n'
        p1 += '<td bgcolor=\"' + color + '\">   ' + str(tabla.tablaActual[simbolo].getColumna()) + '   </td>\n'
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

if __name__=='__main__':
    app.run(host='localhost',debug=True)