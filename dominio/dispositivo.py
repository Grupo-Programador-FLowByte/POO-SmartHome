class Dispositivo:
    def __init__(self, id_dispositivo, nombre, tipo, estado):
        self.__id_dispositivo = id_dispositivo
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado

    @property
    def id_dispositivo(self):
        return self.__id_dispositivo

    def __str__(self):
        return f"Dispositivo(ID: {self.id_dispositivo}, Nombre: {self.nombre}, Tipo: {self.tipo}, Estado: {self.estado})"
