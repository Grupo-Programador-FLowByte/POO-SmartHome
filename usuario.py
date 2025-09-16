usuarios_registrados = []

class Usuario:
   def __init__(self, id_usuario, nombre, usuario, clave, rol):
      self.__id_usuario = id_usuario
      self.nombre = nombre
      self.__usuario = usuario
      self.__clave = clave
      self.rol = rol

   def get_id_usuario(self):
     return self.__id_usuario

   def set_id_usuario(self, id_usuario):
     self.__id_usuario = id_usuario

   def get_usuario(self):
      return self.__usuario

   def set_usuario(self, usuario):
     self.__usuario = usuario

   def get_clave(self):
     return self.__clave

   def set_clave(self, clave):
     self.__clave = clave

   def registrar_usuario(self):
         usuarios_registrados.append(self)
         print(f"Usuario '{self.__usuario}' registrado con éxito.")

   def iniciar_sesion(self, usuario, clave):
      if self.__usuario == usuario and self.__clave == clave:
         print("Inicio de sesión exitoso.")
         return True
      else:
         print("Usuario o clave incorrectos.")
         return False

   def cambiar_rol_usuario(self, nuevo_rol: bool):
     self.rol = nuevo_rol
     print(f"Rol actualizado a: {'Administrador' if nuevo_rol else 'Estandar'}")

   @staticmethod
   def obtener_usuario_por_nombre(nombre_buscado):
      for usuario in usuarios_registrados:
          if usuario.nombre == nombre_buscado:
              return usuario
      return None
