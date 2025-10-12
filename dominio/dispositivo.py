from dominio.usuario import Usuario
from dao.dispositivo_dao import DispositivoDAO

class Dispositivo:
   def __init__(self, id_dispositivo, nombre, tipo, estado,usuario: Usuario):
        self.__id_dispositivo = id_dispositivo
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado
        self.usuario = usuario

   @property
   def id_dispositivo(self):
      return self.__id_dispositivo
   
   @id_dispositivo.setter
   def id_dispositivo(self,id_dispositivo):
      self.__id_dispositivo=id_dispositivo

   def agregar_dispositivo(self):
        
        if not isinstance(self.usuario, Usuario):
            print("Error: el usuario debe ser un objeto de la clase Usuario.")
            return None

        if not self.nombre or not self.tipo:
            print("Error: el nombre y el tipo no pueden estar vacíos.")
            return None

        if not isinstance(self.estado, bool):
            print("Error: el estado debe ser booleano.")
            return None

        return DispositivoDAO.insertar(self.nombre, self.tipo, self.estado, self.usuario)
   
   def listar_dispositivo(self):
        return DispositivoDAO.obtener_todos()
   
   def buscar_dispositivo(self):
       return DispositivoDAO.obtener_por_id(self.id_dispositivo)

   def eliminar_dispositivo(self):
        if not self.id_dispositivo:
            print("Error: el dispositivo no tiene un ID válido.")
            return False

        return DispositivoDAO.eliminar(self.id_dispositivo)

   def __str__(self):
     return (f"Dispositivo:\n  {self.nombre} ({self.id_dispositivo})\n"
            f"  Tipo: {self.tipo}\n"
            f"  Estado: {self.estado}\n"
            f"  Usuario: {self.usuario.nombre}\n"
        )
# ------------------ TAREAS PENDIENTES ------------------
    # 1. agregar_dispositivo:
    #    - Insertar un nuevo dispositivo en la base de datos.
    #    - Recibir: nombre, tipo, estado, usuario.
    #    - Retornar objeto Dispositivo con id_dispositivo asignado.
    #
    # 2. listar_dispositivo:
    #    - Recuperar todos los dispositivos de la base de datos.
    #    - Devolver una lista de objetos Dispositivo.
    #
    # 3. buscar_dispositivo:
    #    - Buscar un dispositivo por id_dispositivo.
    #    - Retornar objeto Dispositivo si existe, o None si no.
    #
    # 4. eliminar_dispositivo:
    #    - Eliminar dispositivo según id_dispositivo.
    #    - Retornar True si se eliminó, False si no se encontró.
    #
    # 5. Métodos opcionales:
    #    - activar/desactivar dispositivo (cambiar estado)
    #    - actualizar dispositivo (modificar nombre, tipo, estado)
    #
    # 6. Integración con DAO:
    #    - Crear DispositivoDAO que maneje conexión a MySQL.
    #    - Métodos de la clase pueden llamar a DAO.
    #
    # 7. Validaciones:
    #    - usuario debe ser objeto Usuario.
    #    - estado debe ser booleano.
    #    - nombre y tipo no vacíos.
