#!/bin/bash

# Paso 4: Dar permisos 777 recursivos a la carpeta 'env' (entorno virtual)
echo "Dando permisos 777 recursivos a la carpeta 'env'..."
sudo chmod -R 777 ./env

# Paso 2: Dar permisos 777 recursivos a la carpeta de datos de MariaDB
echo "Dando permisos 777 recursivos a la carpeta 'mariadb_data'..."
sudo chmod -R 777 ./mariadb_data

# Paso 1: Arrancar los contenedores de BBDD
echo "Arrancando los contenedores de BBDD..."
docker-compose up -d

# Paso 3: Cambiar al directorio de la aplicación
echo "Entrando al directorio 'web'..."
cd web

# Paso 5: Crear el entorno virtual
echo "Creando entorno virtual..."
python3 -m venv env

# Paso 6: Activar el entorno virtual
echo "Activando entorno virtual..."
source env/bin/activate

# Paso 7: Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Paso 8: Ejecutar la aplicación
echo "Ejecutando la aplicación Python..."
python3 app.py