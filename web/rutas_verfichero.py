from __future__ import print_function
from __main__ import app
from flask import request
import os
import sys
import json
import subprocess

@app.route('/ver/<archivo>', methods=['GET'])
def ver_archivo(archivo):
    try:
        basepath = os.path.dirname(__file__)  # Ruta del archivo actual
        ruta_archivo = os.path.join(basepath, 'static', archivo)
        
        if os.path.exists(ruta_archivo):
            salida = subprocess.getoutput(f"cat {ruta_archivo}")
            return json.dumps({"status": "OK", "contenido": salida}), 200
        # else:
        #     return json.dumps({"status": "ERROR", "mensaje": "El archivo no existe"}), 404
    except Exception as e:
        print(f"Error al leer el archivo: {e}", file=sys.stdout)
        return json.dumps({"status": "ERROR"}), 500
