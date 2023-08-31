import os
from functools import wraps
from flask import Flask, jsonify, request
from src import dbmongo as cxmongo



app = Flask(__name__)
# app.config['SECRET_KEY'] = "mitoken"

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome class OPEN endpoint with mongo"})

@app.route('/estudiante', methods=['GET'])
def estudianteget():
    #mi_conexion = cxmongo.dbinfo()#Test connection
    estudiante_codigo = int(request.form['codigo'])
    # print(estudiante_codigo)
    # print('la conexion es')
    # print(mi_conexion)
    # print(estudiante_codigo)
    mi_db = cxmongo.dbConnection()
    mi_coleccion = mi_db.sisdis
    mi_query = {"codigo":estudiante_codigo}
    cursor = mi_coleccion.find(mi_query).limit(1)
    for doc in cursor:
        return jsonify({"Choo Choo": "Retorna informacion del estudiante [nombre]:"+doc['nombre']+" [nota]:"+str(doc['nota'])})
    #return jsonify({"Choo Choo": "No existe informacion del estudiante"})
    #return jsonify({"Choo Choo": "Retorna informacion del estudiante V:"+ str(mi_conexion)})
    return jsonify({"Choo Choo": "NO hay informacion del estudiante"})

@app.route('/estudiante', methods=['POST'])
def estudiantepost():
    try:
        #estudiante_codigo = request.form['codigo'] 
        #estudiante_nombre = request.form['nota']
        ##Realizar metodo update de la nota
        return jsonify({"Choo Choo": "Actualiza nota del estudiante"})
    except Exception as e:
        return jsonify({"message":"Error. " + str(e)}), 400 



"""
MAIN ...........................................................................
"""
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, port=os.getenv("PORT", default=5000 )) 