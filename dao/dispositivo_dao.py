from conn.conexion import obtener_conexion, cerrar_conexion
from dominio.dispositivo import Dispositivo


class DispositivoDAO:

    @staticmethod
    def insertar(nombre, tipo, estado):
        conexion = obtener_conexion()
        if conexion is None:
            return None
        
        cursor = None

        try:
            cursor = conexion.cursor()
            query = """
                INSERT INTO dispositivo (nombre, tipo, estado)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (nombre, tipo, estado))
            conexion.commit()
            id_generado = cursor.lastrowid
            return Dispositivo(id_generado, nombre, tipo, estado)
        except Exception as e:
            print("Error al insertar dispositivo:", e)
            return None
        finally:
            cerrar_conexion(conexion,cursor) 

    @staticmethod
    def obtener_todos():
        conexion = obtener_conexion()
        dispositivos = []
        if conexion is None:
            return dispositivos
        
        cursor = None

        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM dispositivo")
            resultados = cursor.fetchall()
            for fila in resultados:
                dispositivos.append(Dispositivo(
                    fila['id_dispositivo'],
                    fila['nombre'],
                    fila['tipo'],
                    fila['estado']
                ))
            return dispositivos
        except Exception as e:
            print("Error al obtener dispositivos:", e)
            return dispositivos
        finally:
            cerrar_conexion(conexion,cursor)

    @staticmethod
    def obtener_por_id(id_dispositivo):
        conexion = obtener_conexion()
        if conexion is None:
            return None
        
        cursor = None

        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM dispositivo WHERE id_dispositivo = %s", (id_dispositivo,))
            fila = cursor.fetchone()
            if fila:
                return Dispositivo(
                    fila['id_dispositivo'],
                    fila['nombre'],
                    fila['tipo'],
                    fila['estado']
                )
            return None
        except Exception as e:
            print("Error al obtener dispositivo por ID:", e)
            return None
        finally:
            cerrar_conexion(conexion,cursor)

    @staticmethod
    def eliminar(id_dispositivo):
        conexion = obtener_conexion()
        if conexion is None:
            return False
        
        cursor = None

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "DELETE FROM dispositivo WHERE id_dispositivo = %s", (id_dispositivo,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Error al eliminar dispositivo:", e)
            return False
        finally:
            cerrar_conexion(conexion,cursor)
