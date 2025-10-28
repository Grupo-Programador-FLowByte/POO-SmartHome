from enum import Enum


class Rol(Enum):
    ADMIN = "admin"
    ESTANDAR = "estandar"

    @staticmethod
    def from_input(opcion: str):
        """
        Convierte la opción del usuario en un Rol.
        1 => ADMIN
        2 => ESTANDAR
        Cualquier otro valor => ESTANDAR
        """
        if opcion == "1":
            return Rol.ADMIN
        else:
            return Rol.ESTANDAR


class Usuario:
    def __init__(self, id_usuario, nombre, usuario, clave, rol):
        self.__id_usuario = id_usuario
        self.nombre = nombre
        self.__usuario = usuario
        self.__clave = clave
        self.rol = rol

    # ------------------- Getters y Setters -------------------
    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, clave):
        self.__clave = clave

    # ------------------- Métodos de instancia -------------------

    def cambiar_rol(self, nuevo_rol: Rol):
        if isinstance(nuevo_rol, Rol):
            self.rol = nuevo_rol
            print(f"Rol actualizado a: {self.rol.value.upper()}")
        else:
            print("Rol inválido. Se mantiene el rol actual.")

    def verificar_credenciales(self, usuario_input, clave_input) -> bool:
        return self.__usuario == usuario_input and self.__clave == clave_input

    def mostrar_info(self):
        return {
            "id_usuario": self.__id_usuario,
            "nombre": self.nombre,
            "usuario": self.__usuario,
            "rol": self.rol.value
        }


#  prueba
if __name__ == "__main__":
    # Crear usuario
    u = Usuario(1, "Lucas Gómez", "lucas", "1234", "admin")

    # Cambiar rol
    u.cambiar_rol("estandar")

    # Verificar credenciales
    if u.verificar_credenciales("lucas", "1234"):
        print("Inicio de sesión exitoso")
    else:
        print("Usuario o clave incorrectos")

    # Mostrar información
    print(u.mostrar_info())
