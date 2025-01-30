from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_pelicula(titulo, sinopsis, precio, poster):
    try:
        conexion = obtener_conexion()
        iva= calculariva(precio)
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO peliculas(titulo, sinopsis, precio, iva, poster) VALUES (%s, %s, %s, %s, %s)",
                           (titulo, sinopsis, precio, iva, poster))
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}
        code = 200
        conexion.commit()
        conexion.close()
    except:
        print("Excepción al insertar una película", file=sys.stdout)
        ret = {"status": "Failure"}
        code = 500
    return ret, code

def convertir_pelicula_a_json(pelicula):
    d = {}
    d['id'] = pelicula[0]
    d['titulo'] = pelicula[1]
    d['sinopsis'] = pelicula[2]
    d['precio'] = pelicula[3]
    d['iva'] = pelicula[4]
    d['poster'] = pelicula[5]
    
    return d

def obtener_peliculas():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, titulo, sinopsis, precio, iva, poster FROM peliculas")
            peliculas = cursor.fetchall()
            print("LLEGA")
            print(peliculas)
            peliculas_json = []
            if peliculas:
                for pelicula in peliculas:
                    peliculas_json.append(convertir_pelicula_a_json(pelicula))
        conexion.close()
        code = 200
    except:
        print("Excepción al obtener las películas", file=sys.stdout)
        peliculas_json = []
        code = 500
    return peliculas_json, code

def obtener_pelicula_por_id(id):
    pelicula_json = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, titulo, sinopsis, precio, iva, poster FROM peliculas WHERE id = %s", (id,))
            pelicula = cursor.fetchone()
            print("RESULTADOO")
            print(pelicula)
            if pelicula is not None:
                pelicula_json = convertir_pelicula_a_json(pelicula)
        conexion.close()
        code = 200
    except:
        print("Excepción al recuperar una película", file=sys.stdout)
        code = 500
    return pelicula_json, code

def eliminar_pelicula(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM peliculas WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                mensaje = f"Película con ID {id} eliminada correctamente."
                ret = {"status": "OK", "message": mensaje}
            else:
                ret = {"status": "Failure"}
        conexion.commit()
        conexion.close()
        code = 200
    except:
        print("Excepción al eliminar una película", file=sys.stdout)
        ret = {"status": "Failure"}
        code = 500
    return ret, code

def actualizar_pelicula(id, titulo, sinopsis, precio, poster):
    try:
        conexion = obtener_conexion()
        iva= calculariva(precio)
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE peliculas SET titulo = %s, sinopsis = %s, precio = %s, iva=%s, poster = %s WHERE id = %s",
                           (titulo, sinopsis, precio, iva, poster, id))
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}
        conexion.commit()
        conexion.close()
        code = 200
    except:
        print("Excepción al actualizar una película", file=sys.stdout)
        ret = {"status": "Failure"}
        code = 500
    return ret, code

def calculariva(importe):
    return importe*0.21
