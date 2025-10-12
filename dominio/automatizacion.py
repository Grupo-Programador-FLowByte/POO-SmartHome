class Automatizacion:
    def __init__(self, id_automatizacion, nombre, funcionalidad, estado=False):
        self.__id_automatizacion = id_automatizacion
        self.nombre = nombre
        self.funcionalidad = funcionalidad
        self.estado = estado  # False = Inactivo, True = Activo

    @property
    def id_automatizacion(self):
        """Getter para id_automatizacion"""
        return self.__id_automatizacion

    @id_automatizacion.setter
    def id_automatizacion(self, id_automatizacion):
        """Setter para id_automatizacion"""
        self.__id_automatizacion = id_automatizacion

    def activar_modo(self):
        """
        Cambia el estado de la automatización.
        Se usa junto con el DAO para persistir en base de datos.
        """
        self.estado = not self.estado

    def reglas_de_automatizacion(self):
        """Devuelve una descripción de las reglas de la automatización."""
        return f"Reglas de {self.nombre}: {self.funcionalidad}"

    def __str__(self):
        return (f"Automatizacion:\n  {self.nombre} ({self.id_automatizacion})\n"
                f"  Funcionalidad: {self.funcionalidad}\n"
                f"  Estado: {'Activo' if self.estado else 'Inactivo'}\n")



