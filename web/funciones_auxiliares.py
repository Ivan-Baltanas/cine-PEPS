from werkzeug.http import http_date
from flask import session
import json
import decimal
import html
import bleach
import bcrypt
import datetime
# import html
# import bleach
# import bcrypt
# from flask import session


def cipher_password(password):
  hashAndSalt = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(10))
  return hashAndSalt

def compare_password(password_hash,password):
   if password_hash is None:
      return False
   try:
      return bcrypt.checkpw(password,password_hash)
   except:
      return False
   
def sanitize_input(user_input):
 # Usamos bleach para eliminar etiquetas HTML no deseadas
 escaped_input = html.escape(user_input)
 return bleach.clean(escaped_input)    
    
def create_session(usuario,perfil):
    session["usuario"]=usuario
    session["perfil"]=perfil
def delete_session():
    session.clear()

def validar_session_normal():
    try:
        if (session["usuario"] and session["usuario"]!=""):
            return True
        else:
            return False
    except:
        return False