from usuario import Usuario

class Dispositivo:
   def __init__(self, id_dispositivo, nombre, tipo, estado,usuario: Usuario):
        self.__id_dispositivo = id_dispositivo
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado
        self.usuario=usuario

   @property
   def id_dispositivo(self):
      return self.__id_dispositivo
   
   @id_dispositivo.setter
   def id_dispositivo(self,id_dispositivo):
      self.__id_dispositivo=id_dispositivo

   def agregar_dispositivo(self):
       pass
   
   def listar_dispositivo(self):
       pass
   
   def buscar_dispositivo(self):
       pass
   
   def eliminar_dispositivo(self):
       pass

   def __str__(self):
     return (f"Dispositivo:\n  {self.nombre} ({self.id_dispositivo})\n"
            f"  Tipo: {self.tipo}\n"
            f"  Estado: {self.estado}\n"
            f"  Usuario: {self.usuario.nombre}\n"
        )
