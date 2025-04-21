import os
from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
from funciones_auxiliares import prepare_response_extra_headers


app = Flask(__name__)
app.config.from_pyfile('settings.py')
csrf = CSRFProtect(app)
@app.before_request
def csrf_protect():
 if not request.path.startswith("/login") and not request.path.startswith("/registro"):
    csrf.protect()

#Configuración de la cabecera
extra_headers=prepare_response_extra_headers(True)

#Configuración de las sesiones con cookies
app.config.update(PERMANENT_SESSION_LIFETIME=600)
#app.config.update( SESSION_COOKIE_SECURE=True, SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax',) #CON HTTPS
app.config.update( SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax',)  # CON HTTP



import rutas_inicio

import rutas_upload

import rutas_verfichero

import rutas_juegos

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    host = os.environ.get('HOST')
    app.run(host=host, port=port, ssl_context = ('cert.pem','key.pem'))
    
    
    
    