from __future__ import print_function
from app import app
from flask import request, session
from bd import obtener_conexion
import json
import sys
import traceback  # Para capturar trazas de errores
import controlador_usuarios
import funciones_auxiliares import Encoder, sanitize_input,delete_session

@app.route("/login", methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        login_json = request.json
        if "username" in login_json and "password" in login_json:
            username = sanitize_input(login_json['username'])
            password = sanitize_input(login_json['password'])
            if isinstance(username, str) and isinstance(password, str) and len(username) < 50 and len(password) < 50:
                respuesta, code = controlador_usuarios.login_usuario(username, password)
            else:
                respuesta = {"status": "Bad parameters"}
                code = 401
        else:
            respuesta = {"status": "Bad request"}
            code = 401
    else:
        respuesta = {"status": "Bad request"}
        code = 401

    response = make_response(json.dumps(respuesta, cls=Encoder), code)
    return response


@app.route("/registro", methods=['POST'])
def registro():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        login_json = request.json
        if "username" in login_json and "password" in login_json and "profile" in login_json and "email" in login_json:
            username = sanitize_input(login_json['username'])
            password = sanitize_input(login_json['password'])
            profile = sanitize_input(login_json['profile'])
            email = sanitize_input(login_json['email'])

            if isinstance(username, str) and isinstance(password, str) and isinstance(profile, str) and len(username) < 50 and len(password) < 50:
                respuesta, code = controlador_usuarios.alta_usuario(username, password, profile, email)
            else:
                respuesta = {"status": "Bad parameters"}
                code = 401
        else:
            respuesta = {"status": "Bad request"}
            code = 401
    else:
        respuesta = {"status": "Bad request"}
        code = 401

    response = make_response(json.dumps(respuesta, cls=Encoder), code)
    return response


@app.route("/logout", methods=['GET'])
def logout():
    print("Cerrando sesión", file=sys.stdout)
    session.clear()
    print("Sesión cerrada correctamente", file=sys.stdout)
    return json.dumps({"status": "OK"}), 200