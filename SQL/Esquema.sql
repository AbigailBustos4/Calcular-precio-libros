DROP DATABASE gestion_libros;
CREATE DATABASE gestion_libros;
USE gestion_libros;

CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    tipo INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);
