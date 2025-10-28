from abc import ABC, abstractmethod
from dominio.usuario import Usuario, Rol


class IUsuarioDAO(ABC):
    @abstractmethod
    def insertar(self, nombre: str, usuario: str, clave: str, rol: Rol) -> Usuario | None:
        pass

    @abstractmethod
    def obtener_todos(self) -> list[Usuario]:
        pass

    @abstractmethod
    def iniciar_sesion(self, usuario_input: str, clave_input: str) -> Usuario | None:
        pass

    @abstractmethod
    def actualizar_rol(self, id_usuario: int, nuevo_rol: Rol) -> bool:
        pass

    @abstractmethod
    def obtener_por_usuario(self, usuario: str) -> Usuario | None:
        pass
