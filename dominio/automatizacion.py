class Automatizacion:
    def __init__(self, id_automatizacion, nombre, funcionalidad, estado=False):
        self.__id_automatizacion = id_automatizacion
        self.nombre = nombre
        self.funcionalidad = funcionalidad
        self.estado = estado  # False = Inactivo, True = Activo

    @property
    def id_automatizacion(self):
        return self.__id_automatizacion

    @id_automatizacion.setter
    def id_automatizacion(self, id_automatizacion):
        self.__id_automatizacion = id_automatizacion

    def activar_modo(self):
        """Cambia el estado de la automatización."""
        self.estado = not self.estado

    def __str__(self):
        return (f"Automatizacion:\n"
                f"  {self.nombre} ({self.id_automatizacion})\n"
                f"  Funcionalidad: {self.funcionalidad}\n"
                f"  Estado: {'Activo' if self.estado else 'Inactivo'}\n")
