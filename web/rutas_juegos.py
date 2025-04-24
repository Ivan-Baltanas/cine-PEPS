from flask import request, session, make_response
import json
import decimal
from app import app
import controlador_juegos
from funciones_auxiliares import Encoder, sanitize_input, prepare_response_extra_headers,validar_session_admin,validar_session_normal


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): 
            return float(obj)

@app.route("/juegos", methods=["GET"])
def peliculas():
    if (validar_session_normal()):
        peliculas, code = controlador_juegos.obtener_peliculas()
    else:
        peliculas={"status":"Forbidden"}
        code=403
    response=make_response(json.dumps(peliculas),code)
    return response
    if (validar_session_normal()):
        peliculas, code = controlador_juegos.obtener_peliculas()
    else:
        peliculas={"status":"Forbidden"}
        code=403
    response=make_response(json.dumps(peliculas),code)
    return response

@app.route("/juegos/<id>",methods=["GET"])
def pelicula_por_id(id):
    id = sanitize_input(id)
    if isinstance(id, str) and len(id)<64:
        if (validar_session_normal()):
            pelicula, code = controlador_juegos.obtener_pelicula_por_id(id)
        else:
            pelicula={"status":"Forbidden"}
            code=403
    else:
        pelicula={"status":"Bad parameters"}
        code=401
    response= make_response(json.dumps(pelicula, cls=Encoder), code)
    return response

@app.route("/juegos/<id>",methods=["GET"])
def pelicula_por_id(id):
    id = sanitize_input(id)
    if isinstance(id, str) and len(id)<64:
        if (validar_session_normal()):
            pelicula, code = controlador_juegos.obtener_pelicula_por_id(id)
        else:
            pelicula={"status":"Forbidden"}
            code=403
    else:
        pelicula={"status":"Bad parameters"}
        code=401
    response= make_response(json.dumps(pelicula, cls=Encoder), code)
    return response


@app.route("/juegos", methods=["POST"])
def guardar_pelicula():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        pelicula_json = request.json
        if "titulo" in pelicula_json and "sinopsis" in pelicula_json and "poster" in pelicula_json and "precio" in pelicula_json:
            titulo = sanitize_input(pelicula_json["titulo"])
            sinopsis = sanitize_input(pelicula_json["sinopsis"])
            precio = pelicula_json["precio"]
            poster = sanitize_input(pelicula_json["poster"])

            # Validaciones de tipo y longitud
            if isinstance(titulo, str) and isinstance(sinopsis, str) and isinstance(poster, str) and \
               len(titulo) < 128 and len(sinopsis) < 512 and len(poster) < 128:

                if validar_session_admin():
                    precio = float(precio)
                    respuesta, code = controlador_juegos.insertar_pelicula(titulo, sinopsis, precio, poster)
                else:
                    respuesta = {"status": "Forbidden"}
                    code = 403
            else:
                respuesta = {"status": "Bad request"}
                code = 401
        else:
            respuesta = {"status": "Bad request"}
            code = 401
    else:
        respuesta = {"status": "Bad request"}
        code = 401

    response = make_response(json.dumps(respuesta, cls=Encoder), code)
    return response


@app.route("/juegos/<id>", methods=["DELETE"])
def eliminar_pelicula(id):
    ret, code = controlador_juegos.eliminar_pelicula(id)
    response=make_response(json.dumps(ret),code)
    return response


def convertir_pelicula_a_json(pelicula):
    d = {}
    d['id'] = pelicula[0]
    d['titulo'] = sanitize_input(pelicula[1])
    d['sinopsis'] = sanitize_input(pelicula[2])
    d['precio'] = pelicula[3]
    d['poster'] = sanitize_input(pelicula[4])
    return d
    response=make_response(json.dumps(ret),code)
    return response

@app.route("/juegos", methods=["PUT"])
def actualizar_pelicula():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        pelicula_json = request.json
        if "id" in pelicula_json and "titulo" in pelicula_json and "sinopsis" in pelicula_json and "poster" in pelicula_json:
            id = request.json["id"]
            titulo = sanitize_input(pelicula_json["titulo"])
            sinopsis = sanitize_input(pelicula_json["sinopsis"])
            precio = pelicula_json["precio"]
            poster = sanitize_input(pelicula_json["poster"])
            if id.isnumeric() and isinstance(titulo, str) and isinstance(sinopsis, str) and precio.isnumeric() and isinstance(poster, str) and len(id)<8 and len(titulo)<128 and len(sinopsis)<512 and len(poster)<128:
                id=int(id)
                precio=float(precio)
                if (validar_session_normal()):
                    ret,code=controlador_juegos.actualizar_pelicula(id,titulo,sinopsis,precio,poster)
                else: 
                    ret={"status":"Forbidden"}
                    code=403
            else:
                ret={"status":"Bad request"}
                code=401
        else:
            ret={"status":"Bad request"}
            code=401
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

def convertir_pelicula_a_json(pelicula):
    d = {}
    d['id'] = pelicula[0]
    d['titulo'] = sanitize_input(pelicula[1])
    d['sinopsis'] = sanitize_input(pelicula[2])
    d['precio'] = pelicula[3]
    d['poster'] = sanitize_input(pelicula[4])
    return d
    response=make_response(json.dumps(ret),code)
    return response

@app.route("/juegos", methods=["PUT"])
def actualizar_pelicula():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        pelicula_json = request.json
        if "id" in pelicula_json and "titulo" in pelicula_json and "sinopsis" in pelicula_json and "poster" in pelicula_json:
            id = request.json["id"]
            titulo = sanitize_input(chuche_json["titulo"])
            sinopsis = sanitize_input(chuche_json["sinopsis"])
            precio = chuche_json["precio"]
            poster = sanitize_input(chuche_json["poster"])
            if id.isnumeric() and isinstance(titulo, str) and isinstance(sinopsis, str) and precio.isnumeric() and isinstance(poster, str) and len(id)<8 and len(titulo)<128 and len(sinopsis)<512 and len(poster)<128:
                id=int(id)
                precio=float(precio)
                if (validar_session_normal()):
                    ret,code=controlador_juegos.actualizar_pelicula(id,titulo,sinopsis,precio,poster)
                else: 
                    ret={"status":"Forbidden"}
                    code=403
            else:
                ret={"status":"Bad request"}
                code=401
        else:
            ret={"status":"Bad request"}
            code=401
    else:
        ret={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(ret, cls=Encoder), code)
    return response
