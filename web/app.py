import os
from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
from funciones_auxiliares import prepare_response_extra_headers
from logging.config import dictConfig
from logging.handlers import TimedRotatingFileHandler

app = Flask(__name__)
app.config.from_pyfile('settings.py')
csrf = CSRFProtect(app)

# Crear directorio de logs si no existe
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)

@app.before_request
def csrf_protect():
    if not request.path.startswith("/login") and not request.path.startswith("/registro"):
        csrf.protect()

# Configuración de la cabecera
extra_headers = prepare_response_extra_headers(True)

# Configuración de las sesiones con cookies
app.config.update(
    PERMANENT_SESSION_LIFETIME=600,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax'
)

# Configuración mejorada de logging
dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": os.path.join(log_dir, "flask.log"),
            "formatter": "default",
        },
        "time-rotate": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(log_dir, "flask_rotate.log"),
            "when": "midnight",
            "interval": 1,
            "backupCount": 7,
            "formatter": "default",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "time-rotate", "file"]
    }
})

@app.after_request
def afterRequest(response):
    response.headers['Server'] = 'API'
    app.logger.info(
        "path: %s | method: %s | status: %s | size: %s >>> %s",
        request.path,
        request.method,
        response.status,
        response.content_length,
        request.remote_addr,
    )
    response.headers.extend(extra_headers)
    return response

# Importar rutas después de configurar la app
import rutas_inicio
import rutas_upload
import rutas_verfichero
import rutas_juegos

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    host = os.environ.get('HOST', '0.0.0.0')
    app.run(host=host, port=port)