-- CREATE DATABASE IF NOT EXISTS CineApp;
-- USE CineApp;

-- -- Tabla para gestionar las películas
-- CREATE TABLE peliculas (
--     id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     titulo VARCHAR(255) NOT NULL,
--     sinopsis VARCHAR(255) NOT NULL,
--     precio DECIMAL(9,2) NOT NULL,
--     iva    DECIMAL(9,2) NOT NULL,
--     poster VARCHAR(255)
-- );

-- -- Tabla para gestionar los usuarios
-- CREATE TABLE usuarios (
--     usuario VARCHAR(100) NOT NULL PRIMARY KEY,
--     clave VARCHAR(255) NOT NULL,
--     perfil VARCHAR(100) NOT NULL,
--     fechaUltimoAcceso DATE
-- );

-- -- Inserción de un usuario administrador
-- INSERT INTO usuarios (usuario, clave, perfil, fechaUltimoAcceso) 
-- VALUES ('admin', '1234', 'admin', '2022-03-01');


CREATE DATABASE IF NOT EXISTS CineApp;
CREATE USER 'user'@'%' IDENTIFIED BY 'userpw';
GRANT ALL PRIVILEGES ON ciber.* TO 'user'@'%';
FLUSH PRIVILEGES;
USE CineApp;
CREATE TABLE peliculas(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    sinopsis VARCHAR(255) NOT NULL,
    precio DECIMAL(9,2) NOT NULL,
    iva    DECIMAL(9,2) NOT NULL,
	poster VARCHAR(255)
);
CREATE TABLE usuarios(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    fechaUltimoAcceso DATE,
    fechaBloqueo DATE,
    numeroAccesosErroneo INTEGER,
    debeCambiarClave BOOLEAN
);
INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`,`estado`, `correo`,`numeroAccesosErroneo`,`fechaUltimoAcceso`) VALUES ('root','$2b$10$hJtLt4u0SqSf.h3S5Uuev.nu98ARhn.6SpvFCYbc1eeynJmy81cmK', 'admin', 'activo','root@pp.es', 0, '2022-03-01 00:00');