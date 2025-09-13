# test_de_ejemplo.py
# Este archivo contiene los tests para la clase Calculadora usando pytest.
# Flujo TDD:
# 1. Escribí un test que falle (por ejemplo, modificar sumar() para que no haga nada)
# 2. Implementá lo mínimo para que pase
# 3. Refactorizá manteniendo los tests verdes

import pytest
from ejemplo import Calculadora


def test_suma():
    calc = Calculadora()
    # Probamos que la suma funcione
    assert calc.sumar(5) == 5
    assert calc.sumar(3) == 8


def test_resta():
    calc = Calculadora()
    calc.sumar(10)  # Ponemos un valor inicial
    # Probamos que la resta funcione
    assert calc.restar(4) == 6
    assert calc.restar(1) == 5

# Para ejecutar los tests:
# 1. Instalá pytest: pip install pytest
# 2. En la terminal, ejecutá: pytest
# 3. Verificá que todos los tests pasen (verde) en la seccion testing 
