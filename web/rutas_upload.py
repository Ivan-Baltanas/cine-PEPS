from __future__ import print_function
from app import app
from flask import request
import os
import json
import sys

@app.route('/upload', methods=['POST'])
def upload():
    try:
        archivo = request.files['fichero']
        nombre_archivo = request.form.get("nombre")
        basepath = os.path.dirname(__file__)  # Ruta del archivo actual
        ruta_subida = os.path.join(basepath, 'static', nombre_archivo)
        
        print(f"Guardando archivo en: {ruta_subida}", file=sys.stdout)
        archivo.save(ruta_subida)
        ret={"status":"OK"}
        code=200
    except Exception as e:
        print(f"Error al subir el archivo: {e}", file=sys.stdout)
        ret={"status":"ERROR"}
        code=500
    response=make_response(json.dumps(ret),code)
    return response
