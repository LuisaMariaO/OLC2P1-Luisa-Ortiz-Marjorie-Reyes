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
    global entrada
    entrada = data.get('code')
    
    
    try:
        instrucciones = Sintactic.parsear(data.get('code'))
        ast = Three(instrucciones[0])
        tabla = SymbolTable(None,"Global")
        ast.setTablaGlobal = tabla
        
        for instr in instrucciones[0]:
            result = instr.interpretar(ast,tabla)
            if type(result) == Exception:
                ast.updateErrores(result)
        graficarErrores(ast.getErrores()+instrucciones[1])
       # listToStr = ' '.join([str(elem) for elem in instrucciones])
        return jsonify({'ok':True, 'msg':'Data recibida', 'consola':ast.getConsola()}),200
    except:
        return jsonify({'ok':False, 'msg':'No es posible analizar la entrada', 'consola':'Error en el servidor :('}), 409
 
@app.route('/compile',methods=['POST'])
def compile():

    data = request.json
    global entrada
    entrada = data.get('code')
    print(data.get('code'))
    genAux = Generador()
    genAux.cleanAll() #Limpio el código de la ejecución anterior
    generador = genAux.getInstance()
    try:
        instrucciones = SintacticF2.parsear(data.get('code'))
        ast = ThreeFase2(instrucciones)
        tabla = TableFase2(None,"Global")
        ast.setTablaGlobal = tabla
        
        
        for instr in instrucciones[0]:
            result = instr.compilar(ast,tabla)
            if type(result) == ExceptionFase2:
                ast.updateErrores(result)
      
        return jsonify({'ok':True, 'msg':'Data recibida', 'consola':generador.getCode()}),200
    except:
        return jsonify({'ok':False, 'msg':'No es posible analizar la entrada', 'consola':'Error en el servidor :('}), 409
 
def graficarErrores(errores):
    Archivo = open("TablaErrores.dot", "w", encoding="UTF-8")
    p1 = '''digraph {
            node[shape=none]
            n1[label=<
            <table border="1">]
            <tr>
            <td bgcolor=\"honeydew4\"> No. </td>
            <td bgcolor=\"honeydew4\">Descripción</td>
            <td bgcolor=\"honeydew4\">Linea</td>
            <td bgcolor=\"honeydew4\">Columna</td>
            <td bgcolor=\"honeydew4\">Fecha y hora</td>
            </tr>\n'''
    contador = 1
    for er in errores:
        p1 += '<tr>\n' + "<td>" + str(contador) + "</td>\n" +  er.toString() +  '</tr>\n'
        contador += 1
    p1 += '''</table>
    >]
    }'''
    Archivo.write(p1)
    Archivo.close()
    system('dot -Tpng TablaErrores.dot -o TablaErrores.png')

def GetEntrada():
    return entrada

if __name__=='__main__':
    app.run(host='localhost',debug=True)