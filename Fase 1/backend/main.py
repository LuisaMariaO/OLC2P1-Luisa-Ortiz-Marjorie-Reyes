from flask import Flask, request
from flask.json import jsonify

from flask_cors import CORS
import Sintactic
from src.Interpreter.Symbol.three import Three
from src.Interpreter.Symbol.symbolTable import SymbolTable
from src.Interpreter.Exceptions.exception import Exception

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "API is working jus fine! uwu"

@app.route('/parse',methods=['POST'])
def parse():

    data = request.json
    
    print(data.get('code'))
    try:
        instrucciones = Sintactic.parsear(data.get('code'))
        ast = Three(instrucciones)
        tabla = SymbolTable(None)
        ast.setTablaGlobal = tabla
        

        for instr in instrucciones:
            result = instr.interpretar(ast,tabla)
            if type(result) == Exception:
                ast.updateErrores(instr)
       # listToStr = ' '.join([str(elem) for elem in instrucciones])
        return jsonify({'ok':True, 'msg':'Data recibida', 'consola':ast.getConsola()}),200
    except:
        return jsonify({'ok':False, 'msg':'No es posible analizar la entrada', 'consola':'Error en el servidor :('}), 409
 
    

if __name__=='__main__':
    app.run(host='localhost',debug=True)