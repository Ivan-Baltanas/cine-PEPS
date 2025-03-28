import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config.from_pyfile('settings.py')
csrf = CSRFProtect(app)
@app.before_request
def csrf_protect():
 if not request.path.startswith("/login") and not request.path.startswith("/registro"):
 csrf.protect()

import rutas_inicio

import rutas_upload

import rutas_verfichero

import rutas_juegos

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)