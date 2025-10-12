from conn.conexion import obtener_conexion
from dominio.dispositivo import Dispositivo
from dominio.usuario import Usuario
# Para obtener el objeto Usuario si es necesario
from dao.usuario_dao import UsuarioDAO


class DispositivoDAO:

    @staticmethod
    def insertar(nombre: str, tipo: str, estado: bool, usuario: Usuario) ->  Dispositivo | None:

        if not usuario or not usuario.id_usuario:
            print("Error: El usuario no es válido o no tiene ID.")
            return None

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO dispositivos (nombre, tipo, estado, usuario_id) VALUES (%s, %s, %s, %s)"
        valores = (nombre, tipo, estado, usuario.id_usuario)
        cursor.execute(sql, valores)
        conexion.commit()
        id_dispositivo = cursor.lastrowid
        conexion.close()

        return Dispositivo(id_dispositivo, nombre, tipo, estado, usuario)

        

    @staticmethod
    def obtener_todos() -> list[Dispositivo]:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM dispositivos")
        resultados = cursor.fetchall()
        conexion.close()

        dispositivos = []
        for r in resultados:
            usuario = UsuarioDAO.obtener_por_id(r['usuario_id'])
            if usuario:
                dispositivo = Dispositivo(
                    r['id_dispositivo'],
                    r['nombre'],
                    r['tipo'],
                    r['estado'],
                    usuario
                )
                dispositivos.append(dispositivo)
        return dispositivos
    

    @staticmethod
    def obtener_por_id(id_dispositivo: int) -> Dispositivo | None:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        sql = "SELECT * FROM dispositivos WHERE id_dispositivo = %s"
        cursor.execute(sql, (id_dispositivo,))
        resultado = cursor.fetchone()
        conexion.close()

        if resultado:
            usuario = UsuarioDAO.obtener_por_id(resultado['usuario_id'])
            if usuario:
                return Dispositivo(
                    resultado['id_dispositivo'],
                    resultado['nombre'],
                    resultado['tipo'],
                    resultado['estado'],
                    usuario
                )
        return None

    @staticmethod
    def obtener_por_usuario(id_usuario: int) -> list[Dispositivo]:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        sql = "SELECT * FROM dispositivos WHERE usuario_id = %s"
        cursor.execute(sql, (id_usuario,))
        resultados = cursor.fetchall()
        conexion.close()

        dispositivos = []
        usuario = UsuarioDAO.obtener_por_id(id_usuario)

        if usuario:
            for r in resultados:
                dispositivo = Dispositivo(
                    r['id_dispositivo'],
                    r['nombre'],
                    r['tipo'],
                    r['estado'],
                    usuario
                )
                dispositivos.append(dispositivo)

        return dispositivos

    @staticmethod
    def eliminar(id_dispositivo: int) -> bool:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM dispositivos WHERE id_dispositivo = %s"
        cursor.execute(sql, (id_dispositivo,))
        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()
        return eliminado