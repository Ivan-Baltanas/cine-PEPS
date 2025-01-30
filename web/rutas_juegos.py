from flask import request, session
import json
import decimal
from app import app
import controlador_juegos

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): 
            return float(obj)

@app.route("/juegos", methods=["GET"])
def peliculas():
    peliculas, code = controlador_juegos.obtener_peliculas()
    return json.dumps(peliculas, cls=Encoder), code

@app.route("/juegos/<id>", methods=["GET"])
def pelicula_por_id(id):
    pelicula, code = controlador_juegos.obtener_pelicula_por_id(id)
    return json.dumps(pelicula, cls=Encoder), code

@app.route("/juegos", methods=["POST"])
def guardar_pelicula():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        pelicula_json = request.json
        ret, code = controlador_juegos.insertar_pelicula(
            pelicula_json["titulo"], 
            pelicula_json["sinopsis"], 
            float(pelicula_json["precio"]), 
            pelicula_json["poster"]
        )
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

@app.route("/juegos/<id>", methods=["DELETE"])
def eliminar_pelicula(id):
    ret, code = controlador_juegos.eliminar_pelicula(id)
    return json.dumps(ret), code

@app.route("/juegos", methods=["PUT"])
def actualizar_pelicula():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        pelicula_json = request.json
        ret, code = controlador_juegos.actualizar_pelicula(
            pelicula_json["id"], 
            pelicula_json["titulo"], 
            pelicula_json["sinopsis"], 
            float(pelicula_json["precio"]), 
            pelicula_json["poster"]
        )
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code
