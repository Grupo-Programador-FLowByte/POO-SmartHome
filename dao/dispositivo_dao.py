from conn.conexion import obtener_conexion
from dominio.dispositivo import Dispositivo
from dominio.usuario import Usuario
# Para obtener el objeto Usuario si es necesario
from dao.usuario_dao import UsuarioDAO


class DispositivoDAO:

    @staticmethod
    def insertar(nombre: str, tipo: str, estado: bool, usuario: Usuario) -> Dispositivo:
        """
        Inserta un nuevo dispositivo en la base de datos y devuelve el objeto Dispositivo creado.
        """
        pass

    @staticmethod
    def obtener_todos() -> list[Dispositivo]:
        """
        Devuelve una lista con todos los dispositivos de la base de datos.
        """
        pass

    @staticmethod
    def obtener_por_id(id_dispositivo: int) -> Dispositivo | None:
        """
        Devuelve un dispositivo según su ID, o None si no existe.
        """
        pass

    @staticmethod
    def obtener_por_usuario(id_usuario: int) -> list[Dispositivo]:
        """
        Devuelve todos los dispositivos de un usuario específico.
        """
        pass

    @staticmethod
    def eliminar(id_dispositivo: int) -> bool:
        """
        Elimina un dispositivo según su ID. Devuelve True si se eliminó.
        """
        pass
