import pytest
from dispositivo import Dispositivo
from usuario import Usuario

def test_nuevo_dispositivo():
    id_dispositivo = 1990
    nombre = "sensor puerta"
    tipo = "sensor"
    estado = "encendido"
    usuario= Usuario(100,"Carlos Gonzalez","carlos","clave100","estandar")
    
    dispositivo = Dispositivo(id_dispositivo, nombre, tipo, estado,usuario)
    
    assert dispositivo.id_dispositivo == id_dispositivo
    assert dispositivo.nombre == nombre
    assert dispositivo.tipo == tipo
    assert dispositivo.estado == estado

def test_estado():
    usuario= Usuario(101,"Juan Perez","juan","clave101","estandar")
    dispositivo = Dispositivo(1991, "Luz Garage", "luz", "apagado",usuario)
    assert dispositivo.estado == "apagado"