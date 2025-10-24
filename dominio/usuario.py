class Usuario:
    def __init__(self, id_usuario, nombre, usuario, clave, rol):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__usuario = usuario
        self.__clave = clave
        self.__rol = rol

    # ------------------- Getters y Setters -------------------
    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

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

    @property
    def rol(self):
        return self.__rol    
    
    @rol.setter
    def rol(self, rol):
        self.__rol = rol

    # ------------------- Métodos de instancia -------------------
    def cambiar_rol(self, nuevo_rol: str):
        """
        Cambia el rol del usuario a 'admin' o 'estandar'.
        """
        if nuevo_rol.lower() in ["admin", "estandar"]:
            self.__rol = nuevo_rol.lower()
            print(f"Rol actualizado a: {self.__rol.upper()}")
        else:
            print("Rol inválido. Debe ser 'admin' o 'estandar'.")

    def verificar_credenciales(self, usuario_input, clave_input) -> bool:
        """
        Verifica si las credenciales coinciden con este usuario.
        """
        return self.__usuario == usuario_input and self.__clave == clave_input

    def mostrar_info(self):
        """
        Devuelve un diccionario con la información del usuario (sin la clave).
        """
        return {
            "id_usuario": self.__id_usuario,
            "nombre": self.__nombre,
            "usuario": self.__usuario,
            "rol": self.__rol
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
