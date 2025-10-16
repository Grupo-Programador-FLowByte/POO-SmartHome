import pytest
from automatizacion import Automatizacion

def test_creacion_automatizacion():
    auto = Automatizacion(1, "Luces", "Encender luces al anochecer")
    assert auto.id_automatizacion == 1
    assert auto.nombre == "Luces"
    assert auto.funcionalidad == "Encender luces al anochecer"
    assert auto.estado is False

def test_activar_modo_por_defecto():
    auto = Automatizacion(2, "Riego", "Activar riego automático")
    auto.activar_modo()
    assert auto.estado is True

def test_activar_modo_false():
    auto = Automatizacion(3, "Cámara", "Grabar movimiento", True)
    auto.activar_modo(False)
    assert auto.estado is False

def test_reglas_de_automatizacion():
    auto = Automatizacion(4, "Persianas", "Bajar persianas al anochecer")
    reglas = auto.reglas_de_automatizacion()
    assert "Persianas" in reglas
    assert "Bajar persianas al anochecer" in reglas

def test_setter_getter_id():
    auto = Automatizacion(5, "Alarma", "Activar sirena en intrusión")
    auto.id_automatizacion = 99
    assert auto.id_automatizacion == 99