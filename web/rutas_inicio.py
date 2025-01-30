from __future__ import print_function
from app import app
from flask import request, session
from bd import obtener_conexion
import json
import sys
import traceback  # Para capturar trazas de errores

@app.route("/login", methods=['POST'])
def login():
    print("Se recibió una solicitud POST en /login", file=sys.stdout)
    content_type = request.headers.get('Content-Type')
    print(f"Content-Type recibido: {content_type}", file=sys.stdout)
    
    if content_type == 'application/json':
        usuario_json = request.json
        print(f"Payload recibido: {usuario_json}", file=sys.stdout)
        
        username = usuario_json.get('username')
        password = usuario_json.get('password')
        print(f"Usuario: {username}, Contraseña: {password}", file=sys.stdout)
        
        try:
            conexion = obtener_conexion()
            print("Conexión a la base de datos establecida", file=sys.stdout)
            
            with conexion.cursor() as cursor:
                print("Ejecutando consulta SQL para validar usuario...", file=sys.stdout)
                cursor.execute(
                    "SELECT perfil FROM usuarios WHERE usuario = %s and clave = %s", 
                    (username, password)
                )
                usuario = cursor.fetchone()
                print(f"Resultado de la consulta: {usuario}", file=sys.stdout)
            
            conexion.close()
            print("Conexión a la base de datos cerrada", file=sys.stdout)
            
            if usuario is None:
                ret = {"status": "ERROR", "mensaje": "Usuario o contraseña incorrectos"}
                print("Usuario no encontrado o credenciales incorrectas", file=sys.stdout)
            else:
                ret = {"status": "OK"}
                #session["usuario"] = username
               # session["perfil"] = usuario[0]
                print(f"Sesión iniciada para el usuario: {username}, Perfil: {usuario[0]}", file=sys.stdout)
            code = 200
        except Exception as e:
            print("Excepción al validar al usuario:", file=sys.stdout)
            print(traceback.format_exc(), file=sys.stdout)  # Muestra la traza del error
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
        print("El Content-Type no es application/json", file=sys.stdout)
    
    print(f"Respuesta enviada: {ret}, Código HTTP: {code}", file=sys.stdout)
    return json.dumps(ret), code

@app.route("/registro", methods=['POST'])
def registro():
    print("Se recibió una solicitud POST en /registro", file=sys.stdout)
    content_type = request.headers.get('Content-Type')
    print(f"Content-Type recibido: {content_type}", file=sys.stdout)
    
    if content_type == 'application/json':
        usuario_json = request.json
        print(f"Payload recibido: {usuario_json}", file=sys.stdout)
        
        username = usuario_json.get('username')
        password = usuario_json.get('password')
        perfil = usuario_json.get('profile')
        print(f"Usuario: {username}, Contraseña: {password}, Perfil: {perfil}", file=sys.stdout)
        
        try:
            conexion = obtener_conexion()
            print("Conexión a la base de datos establecida", file=sys.stdout)
            
            with conexion.cursor() as cursor:
                print("Ejecutando consulta SQL para verificar si el usuario ya existe...", file=sys.stdout)
                cursor.execute(
                    "SELECT perfil FROM usuarios WHERE usuario = %s", 
                    (username,)
                )
                usuario = cursor.fetchone()
                print(f"Resultado de la consulta: {usuario}", file=sys.stdout)
                
                if usuario is None:
                    print("Usuario no encontrado, insertando nuevo usuario...", file=sys.stdout)
                    cursor.execute(
                        "INSERT INTO usuarios(usuario, clave, perfil) VALUES(%s, %s, %s)", 
                        (username, password, perfil)
                    )
                    if cursor.rowcount == 1:
                        conexion.commit()
                        ret = {"status": "OK"}
                        code = 200
                        print(f"Usuario {username} registrado correctamente", file=sys.stdout)
                    else:
                        ret = {"status": "ERROR"}
                        code = 500
                        print("Error al registrar el usuario", file=sys.stdout)
                else:
                    ret = {"status": "ERROR", "mensaje": "El usuario ya existe"}
                    code = 200
                    print(f"El usuario {username} ya existe", file=sys.stdout)
            
            conexion.close()
            print("Conexión a la base de datos cerrada", file=sys.stdout)
        except Exception as e:
            print("Excepción al registrar al usuario:", file=sys.stdout)
            print(traceback.format_exc(), file=sys.stdout)  # Muestra la traza del error
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
        print("El Content-Type no es application/json", file=sys.stdout)
    
    print(f"Respuesta enviada: {ret}, Código HTTP: {code}", file=sys.stdout)
    return json.dumps(ret), code

@app.route("/logout", methods=['GET'])
def logout():
    print("Cerrando sesión", file=sys.stdout)
    session.clear()
    print("Sesión cerrada correctamente", file=sys.stdout)
    return json.dumps({"status": "OK"}), 200