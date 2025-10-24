class Automatizacion:
    def __init__(self, id_automatizacion, nombre, funcionalidad, estado=False):
        self.__id_automatizacion = id_automatizacion
        self.__nombre = nombre
        self.__funcionalidad = funcionalidad
        self.__estado = estado  # False = Inactivo, True = Activo

    @property
    def id_automatizacion(self):
        return self.__id_automatizacion

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def funcionalidad(self):
        return self.__funcionalidad
    
    @funcionalidad.setter
    def funcionalidad(self, funcionalidad):
        self.__funcionalidad = funcionalidad

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado


    def activar_modo(self):
        """Cambia el estado de la automatización."""
        self.__estado = not self.__estado

    def reglas_de_automatizacion(self):
        """Devuelve una descripción de las reglas de la automatización."""
        return f"Reglas de {self.__nombre}: {self.__funcionalidad}"
    


    def __str__(self):
        return (f"Automatizacion:\n"
                f"  {self.__nombre} ({self.__id_automatizacion})\n"
                f"  Funcionalidad: {self.__funcionalidad}\n"
                f"  Estado: {'Activo' if self.__estado else 'Inactivo'}\n")

