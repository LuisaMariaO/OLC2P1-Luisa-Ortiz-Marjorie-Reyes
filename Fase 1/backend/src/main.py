from flask import Flask, request
from flask.json import jsonify
from xml.etree import ElementTree as ET
import re
from datetime import datetime
import xmltodict
import json
from flask_cors import CORS
import Sintactic

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
        listToStr = ' '.join([str(elem) for elem in instrucciones])
        return jsonify({'ok':True, 'msg':'Data recibida', 'consola':listToStr}),200
    except:
        return jsonify({'ok':False, 'msg':'No es posible analizar la entrada', 'consola':'Error en el servidor :('}), 409
 
    

if __name__=='__main__':
    app.run(host='localhost',debug=True)