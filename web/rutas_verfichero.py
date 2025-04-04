from __future__ import print_function
from app import app
from flask import request
import os
import sys
import json
import subprocess

@app.route('/ver/<archivo>', methods=['GET'])
def ver_archivo(archivo):
    try:
        if (validar_session_normal()):
            basepath = os.path.dirname(__file__)  # Ruta del archivo actual
            ruta_archivo = os.path.join(basepath, 'static', archivo)
            
            # if os.path.exists(ruta_archivo):
            salida = subprocess.getoutput(f"cat {ruta_archivo}")
            ret={"status":"OK", "contenido": salida}
            code=200
        else:
            ret={"status":"Forbidden"}
            code=403
    except:
        ret= {"status": "ERROR"}
        code=500
    response=make_response(json.dumps(ret),code)
    return response