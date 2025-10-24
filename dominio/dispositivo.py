class Dispositivo:
    def __init__(self, id_dispositivo, nombre, tipo, estado):
        self.__id_dispositivo = id_dispositivo
        self.__nombre = nombre
        self.__tipo = tipo
        self.__estado = estado

    @property
    def id_dispositivo(self):
        return self.__id_dispositivo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado    
    

    def __str__(self):
        return f"Dispositivo(ID: {self.__id_dispositivo}, Nombre: {self.__nombre}, Tipo: {self.__tipo}, Estado: {self.__estado})"
