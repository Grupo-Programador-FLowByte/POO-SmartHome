CREATE DATABASE IF NOT EXISTS smart_home;
USE smart_home;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    clave VARCHAR(50) NOT NULL,
    rol VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS dispositivo (
    id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS automatizaciones (
    id_automatizacion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    funcionalidad TEXT NOT NULL,
    estado BOOLEAN NOT NULL DEFAULT FALSE
);



-- -----------------------
-- Inserción de usuarios
-- -----------------------
INSERT INTO usuarios (nombre, usuario, clave, rol) VALUES
('Lucas Gómez', 'lucasg', 'pass123', 'admin'),
('Franco Pérez', 'francop', 'pass123', 'estandar'),
('Valentino Díaz', 'valentd', 'pass123', 'estandar'),


-- -----------------------
-- Inserción de dispositivos
-- -----------------------
INSERT INTO dispositivo (nombre, tipo, estado) VALUES
('Luz Cocina', 'luz', FALSE),
('Luz Sala', 'luz', TRUE),
('Luz Habitación', 'luz', TRUE),
('Sensor Puerta', 'sensor', TRUE),
('Alarma Principal', 'alarma', TRUE),
('Luz Baño', 'luz', TRUE),
('Termostato Sala', 'termostato', TRUE),
('Termostato Habitación', 'termostato', FALSE),
('Sensor Ventana', 'sensor', FALSE),
('Aire Acondicionado Sala', 'aire', TRUE),
('Aire Acondicionado Habitación', 'aire', FALSE),
('Cámara Entrada', 'camara', TRUE),
('Cámara Patio', 'camara', FALSE),
('Enchufe Smart Cocina', 'enchufe', FALSE),
('Enchufe Smart Sala', 'enchufe', TRUE),
('Persiana Habitación', 'persiana', FALSE),
('Persiana Sala', 'persiana', TRUE),
('Luz Jardín', 'luz', FALSE),
('Alarma Secundaria', 'alarma', FALSE),
('Riego Jardín', 'riego', TRUE);

-- -----------------------
-- Inserción de automatizaciones
-- -----------------------
INSERT INTO automatizaciones (nombre, funcionalidad, estado) VALUES
('Apagar luces', 'Apaga todas las luces a las 23:00', TRUE),
('Encender termostato', 'Enciende el termostato a las 6:00', TRUE),
('Activar alarma', 'Activa alarma al salir de casa', TRUE),
('Modo ahorro energía', 'Apaga dispositivos inactivos', TRUE);

-- -----------------------
-- Consultas simples
-- -----------------------

SELECT * FROM usuarios;


SELECT * FROM dispositivo;


SELECT * FROM automatizaciones;

