# SECRET_KEY = 'you-will-never-guess'
import os

DEBUG=False  #en producción se pone a false
SECRET_KEY=os.environ.get('SECRET_KEY') # salt para las hash
WTF_CSRF_SECRET_KEY=os.environ.get('WTF_CSRF_SECRET_KEY')   # salt para generar el token
WTF_CSRF_CHECK_DEFAULT=False  #el token csrf se debe controlar sólo si se especifica