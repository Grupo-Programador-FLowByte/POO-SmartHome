from dominio.automatizacion import Automatizacion
from conn.conexion import obtener_conexion



class AutomatizacionDAO:

    @staticmethod
    def obtener_todos() -> list[Automatizacion]:
        """Devuelve todas las automatizaciones de la base de datos."""
        pass

    @staticmethod
    def obtener_por_id(id_automatizacion: int) -> Automatizacion | None:
        """Busca una automatización por su ID en la base de datos."""
        pass

    @staticmethod
    def activar_modo(id_automatizacion: int):
        """Activa o desactiva la automatización según su estado actual."""
        pass

    @staticmethod
    def insertar(nombre: str, funcionalidad: str, estado=False) -> Automatizacion:
        """Inserta una nueva automatización en la base de datos."""
        pass



