class Automatizacion:
    def __init__(self, id_automatizacion, nombre, funcionalidad, estado=False):
        self.__id_automatizacion = id_automatizacion  
        self.nombre = nombre
        self.funcionalidad = funcionalidad
        self.estado = estado

    @property
    def id_automatizacion(self):
        """Getter para id_automatizacion"""
        return self.__id_automatizacion

    @id_automatizacion.setter
    def id_automatizacion(self, id_automatizacion):
        """Setter para id_automatizacion"""
        self.__id_automatizacion = id_automatizacion

    def activar_modo(self, activar=True):
        """Activa o desactiva la automatización (por defecto la activa)."""
        self.estado = activar

    def reglas_de_automatizacion(self):
        """Devuelve una descripción de las reglas de la automatización."""
        return f"Reglas de {self.nombre}: {self.funcionalidad}"
    
"""
Tareas de Valentino

Clase Automatizacion

1. Crear la clase Automatizacion con los siguientes atributos:
   - id_automatizacion
   - nombre
   - funcionalidad
   - estado

2. Implementar métodos:
   - activar_modo()
   - reglas_de_automatizacion()
   - getter

3. Crear los tests en tests/test_automatizacion.py siguiendo TDD:
   - Primero escribir tests que fallen.
   - Luego implementar métodos para pasar los tests.
"""
