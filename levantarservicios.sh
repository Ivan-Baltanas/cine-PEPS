#!/bin/bash

# Paso 1: Arrancar los contenedores de BBDD
echo "Arrancando los contenedores de BBDD..."
docker-compose up -d

# Paso 2: Cambiar al directorio de la aplicación
echo "Entrando al directorio 'web'..."
cd web

# Paso 3: Crear el entorno virtual
echo "Creando entorno virtual..."
python3 -m venv env

# Paso 4: Activar el entorno virtual
echo "Activando entorno virtual..."
source env/bin/activate

# Paso 5: Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Paso 6: Ejecutar la aplicación
echo "Ejecutando la aplicación Python..."
python app.py