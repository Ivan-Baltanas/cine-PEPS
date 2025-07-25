from werkzeug.http import http_date
from flask import session
import json
import decimal
import html
import bleach
import bcrypt
import datetime

def cipher_password(password):
    hashAndSalt = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(10))
    return hashAndSalt

def compare_password(password_hash, password):
    if password_hash is None:
        return False
    try:
        return bcrypt.checkpw(password, password_hash)
    except:
        return False

def sanitize_input(user_input):
    escaped_input = html.escape(user_input)
    return bleach.clean(escaped_input)

def create_session(usuario, perfil):
    session["usuario"] = usuario
    session["perfil"] = perfil

def delete_session():
    session.clear()

def validar_session_normal():
    try:
        if session["usuario"] and session["usuario"] != "":
            return True
        else:
            return False
    except:
        return False

def validar_session_admin():
    try:
        if session["usuario"] and session["usuario"] != "" and session["perfil"] == "admin":
            return True
        else:
            return False
    except:
        return False

def prepare_response_extra_headers(include_security_headers):
    response_extra_headers = {
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0',
        'Last-Modified': http_date(datetime.datetime.now()),
        'Server': ''
    }
    
    if include_security_headers:
        response_security_headers = {
            'X-Frame-Options': 'SAMEORIGIN',
            'Strict-Transport-Security': 'max-age=63072000; includeSubdomains',
            'X-Content-Type-Options': 'nosniff',
            'X-XSS-Protection': '1; mode=block'
        }
        response_extra_headers.update(response_security_headers)
    
    return response_extra_headers