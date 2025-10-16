from dominio.automatizacion import Automatizacion

class AutomatizacionDAO:
    automatizaciones = []  # Lista temporal, luego se puede cambiar a MySQL

    @staticmethod
    def insertar(nombre, funcionalidad, estado=False):
        auto = Automatizacion(len(AutomatizacionDAO.automatizaciones) + 1, nombre, funcionalidad, estado)
        AutomatizacionDAO.automatizaciones.append(auto)
        return auto

    @staticmethod
    def obtener_todos():
        return AutomatizacionDAO.automatizaciones

    @staticmethod
    def obtener_por_id(id_automatizacion):
        for a in AutomatizacionDAO.automatizaciones:
            if a.id_automatizacion == id_automatizacion:
                return a
        return None

    @staticmethod
    def activar_modo(id_automatizacion):
        auto = AutomatizacionDAO.obtener_por_id(id_automatizacion)
        if auto:
            auto.activar_modo(not auto.estado)
            return True
        return False

    @staticmethod
    def eliminar(id_automatizacion):
        auto = AutomatizacionDAO.obtener_por_id(id_automatizacion)
        if auto:
            AutomatizacionDAO.automatizaciones.remove(auto)
            return True
        return False

from conn.conexion import obtener_conexion, cerrar_conexion
from dominio.automatizacion import Automatizacion


class AutomatizacionDAO:

    @staticmethod
    def insertar(nombre, funcionalidad, estado=False):
        conexion = obtener_conexion()
        if conexion is None:
            return None
        try:
            cursor = conexion.cursor()
            query = """
                INSERT INTO automatizaciones (nombre, funcionalidad, estado)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (nombre, funcionalidad, estado))
            conexion.commit()
            id_generado = cursor.lastrowid
            return Automatizacion(id_generado, nombre, funcionalidad, estado)
        except Exception as e:
            print("Error al insertar automatización:", e)
            return None
        finally:
            cerrar_conexion(conexion)

    @staticmethod
    def obtener_todos():
        conexion = obtener_conexion()
        automatizaciones = []
        if conexion is None:
            return automatizaciones
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM automatizaciones")
            resultados = cursor.fetchall()
            for fila in resultados:
                automatizaciones.append(Automatizacion(
                    fila['id_automatizacion'],
                    fila['nombre'],
                    fila['funcionalidad'],
                    fila['estado']
                ))
            return automatizaciones
        except Exception as e:
            print("Error al obtener automatizaciones:", e)
            return automatizaciones
        finally:
            cerrar_conexion(conexion)

    @staticmethod
    def obtener_por_id(id_automatizacion):
        conexion = obtener_conexion()
        if conexion is None:
            return None
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM automatizaciones WHERE id_automatizacion = %s",
                (id_automatizacion,))
            fila = cursor.fetchone()
            if fila:
                return Automatizacion(
                    fila['id_automatizacion'],
                    fila['nombre'],
                    fila['funcionalidad'],
                    fila['estado']
                )
            return None
        except Exception as e:
            print("Error al obtener automatización por ID:", e)
            return None
        finally:
            cerrar_conexion(conexion)

    @staticmethod
    def activar_modo(id_automatizacion):
        """
        Cambia el estado de la automatización y lo persiste en la base de datos.
        """
        auto = AutomatizacionDAO.obtener_por_id(id_automatizacion)
        if not auto:
            return False

        auto.activar_modo()
        conexion = obtener_conexion()
        if conexion is None:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE automatizaciones SET estado = %s WHERE id_automatizacion = %s",
                (auto.estado, id_automatizacion)
            )
            conexion.commit()
            return True
        except Exception as e:
            print("Error al activar/desactivar automatización:", e)
            return False
        finally:
            cerrar_conexion(conexion)





