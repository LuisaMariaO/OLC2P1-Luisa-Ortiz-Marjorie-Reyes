from flask import Flask, request
from flask.json import jsonify
from os import system
from flask_cors import CORS

import Sintactic
import SintacticF2
from src.Interpreter.Symbol.three import Three
from src.Interpreter.Symbol.symbolTable import SymbolTable
from src.Interpreter.Exceptions.exception import Exception
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
    entrada = data.get('code')
    
    try:
        instrucciones = Sintactic.parsear(data.get('code'))
        ast = Three(instrucciones[0])
        tabla = SymbolTable(None,"Global")
        ast.setTablaGlobal = tabla
        
        for instr in ast.getInstrucciones():
            result = instr.interpretar(ast,tabla)
            if type(result) == Exception:
                ast.updateErrores(result)
        graficarErrores(ast.getErrores()+instrucciones[1])
        treeGraph = ast.getTree()
        graficarArbol(treeGraph)
        graficarTabla(tabla)
       # listToStr = ' '.join([str(elem) for elem in instrucciones])
        return jsonify({'ok':True, 'msg':'Data recibida', 'consola':ast.getConsola()}),200
    except:
        return jsonify({'ok':False, 'msg':'No es posible analizar la entrada', 'consola':'Error en el servidor :('}), 409
 
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