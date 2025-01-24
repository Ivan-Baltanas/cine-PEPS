CREATE DATABASE IF NOT EXISTS CineApp;
USE CineApp;

-- Tabla para gestionar las películas
CREATE TABLE peliculas (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    sinopsis VARCHAR(255) NOT NULL,
    precio DECIMAL(9,2) NOT NULL,
    poster VARCHAR(255)
);

-- Tabla para gestionar los usuarios
CREATE TABLE usuarios (
    usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    fechaUltimoAcceso DATE
);

-- Inserción de un usuario administrador
INSERT INTO usuarios (usuario, clave, perfil, fechaUltimoAcceso) 
VALUES ('admin', '1234', 'admin', '2022-03-01');
