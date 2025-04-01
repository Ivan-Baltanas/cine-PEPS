from __future__ import print_function
from app import app
from flask import request
import os
import json
import sys

# @app.route('/upload', methods=['POST'])
# def upload():
#     try:
#         archivo = request.files['fichero']
#         user_input = request.form.get("nombre")
#         basepath = os.path.dirname(__file__)  # Ruta del archivo actual
#         ruta_subida = os.path.join(basepath, 'static', user_input)
        
#         print(f"Guardando archivo en: {ruta_subida}", file=sys.stdout)
#         archivo.save(ruta_subida)
#         return json.dumps({"status": "OK"}), 200
#     except Exception as e:
#         print(f"Error al subir el archivo: {e}", file=sys.stdout)
#         return json.dumps({"status": "ERROR"}), 500

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if validar_session_normal():
            archivo = request.files['fichero']  # Variable renombrada
            nombre_archivo = request.form.get("nombre")  # Variable renombrada

            basepath = os.path.dirname(__file__)  # Ruta del archivo actual
            ruta_subida = os.path.join(basepath, 'static', nombre_archivo)  # Variable renombrada
            
            print(f"Guardando archivo en: {ruta_subida}", file=sys.stdout)
            archivo.save(ruta_subida)
            
            respuesta = {"status": "OK"}
            code = 200
        else:
            respuesta = {"status": "Forbidden"}
            code = 403
    except Exception as e:
        print(f"Error al subir el archivo: {e}", file=sys.stdout)
        respuesta = {"status": "ERROR"}
        code = 500

    response = make_response(json.dumps(respuesta), code)
    return response
