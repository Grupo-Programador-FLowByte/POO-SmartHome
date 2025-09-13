# POO-SmartHome - Programación con TDD

Este proyecto contiene la implementación de clases principales de un sistema SmartHome en Python, siguiendo el enfoque de **Desarrollo Guiado por Pruebas (TDD)**.

## Contenido

- `usuario.py` → Clase `Usuario` con atributos y métodos para gestionar dispositivos.
- `dispositivo.py` → Clase `Dispositivo` con atributos y métodos relacionados.
- `automatizacion.py` → Clase `Automatizacion` con atributos y métodos para controlar automatizaciones.
- `tests/` → Carpeta con tests unitarios para cada clase utilizando **pytest**.

# Para ejecutar los tests:
# 1. Instalá pytest: pip install pytest
# 2. En la terminal, ejecutá: pytest
# 3. Verificá que todos los tests pasen (verde)

Los tests verifican que los métodos de las clases funcionen correctamente:  
- Si un test falla, significa que la funcionalidad aún no cumple con lo esperado.  
- Si todos los tests pasan, la funcionalidad está correcta.

## Flujo TDD

1. **Escribir un test que falle**: define la funcionalidad que queremos implementar.  
2. **Implementar lo mínimo** para pasar el test.  
3. **Refactorizar** el código manteniendo los tests funcionando.  
4. Repetir el ciclo para cada nueva funcionalidad.

## Notas

- La estructura permite agregar fácilmente nuevas clases y tests.  
- Los tests aseguran que los cambios futuros no rompan funcionalidades existentes.
