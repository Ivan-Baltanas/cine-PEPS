from __future__ import print_function
from __main__ import app
from flask import request, session
from bd import obtener_conexion
import json
import sys

@app.route("/login", methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        usuario_json = request.json
        username = usuario_json['username']
        password = usuario_json['password']
        try:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                cursor.execute(
                    "SELECT perfil FROM usuarios WHERE usuario = %s and clave = %s", 
                    (username, password)
                )
                usuario = cursor.fetchone()
            conexion.close()
            if usuario is None:
                ret = {"status": "ERROR", "mensaje": "Usuario o contraseña incorrectos"}
            else:
                ret = {"status": "OK"}
                session["usuario"] = username
                session["perfil"] = usuario[0]
            code = 200
        except Exception as e:
            print("Excepción al validar al usuario:", e, file=sys.stdout)
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

@app.route("/registro", methods=['POST'])
def registro():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        usuario_json = request.json
        username = usuario_json['username']
        password = usuario_json['password']
        perfil = usuario_json['profile']
        try:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                cursor.execute(
                    "SELECT perfil FROM usuarios WHERE usuario = %s", 
                    (username,)
                )
                usuario = cursor.fetchone()
                if usuario is None:
                    print(f"INSERT INTO usuarios(usuario,clave,perfil) VALUES('{username}','{password}','{perfil}')")
                    cursor.execute(
                        "INSERT INTO usuarios(usuario,clave,perfil) VALUES(%s, %s, %s)", 
                        (username, password, perfil)
                    )
                    if cursor.rowcount == 1:
                        conexion.commit()
                        ret = {"status": "OK"}
                        code = 200
                    else:
                        ret = {"status": "ERROR"}
                        code = 500
                else:
                    ret = {"status": "ERROR", "mensaje": "El usuario ya existe"}
                    code = 200
            conexion.close()
        except Exception as e:
            print("Excepción al registrar al usuario:", e, file=sys.stdout)
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

@app.route("/logout", methods=['GET'])
def logout():
    session.clear()
    return json.dumps({"status": "OK"}), 200
