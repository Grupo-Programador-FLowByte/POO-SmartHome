from dao.Interfaces.i_usuario_dao import IUsuarioDAO
from conn.conexion import obtener_conexion, cerrar_conexion
from dominio.usuario import Usuario, Rol


class UsuarioDAO(IUsuarioDAO):


    @staticmethod
    def insertar(nombre: str, usuario: str, clave: str, rol: Rol) -> Usuario | None:
        conexion = obtener_conexion()
        if conexion is None:
            return None

        cursor = None
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO usuarios (nombre, usuario, clave, rol) VALUES (%s, %s, %s, %s)"
            valores = (nombre, usuario, clave, rol.value)
            cursor.execute(sql, valores)
            conexion.commit()
            id_usuario = cursor.lastrowid
            return Usuario(id_usuario, nombre, usuario, clave, rol)
        except Exception as e:
            print("Error al insertar usuario:", e)
            return None
        finally:
            cerrar_conexion(conexion, cursor)

    @staticmethod
    def obtener_todos() -> list[Usuario]:
        conexion = obtener_conexion()
        usuarios = []
        if conexion is None:
            return usuarios

        cursor = None
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios")
            resultados = cursor.fetchall()
            for r in resultados:
                rol_enum = Rol(r['rol'])
                usuarios.append(
                    Usuario(r['id_usuario'], r['nombre'], r['usuario'], r['clave'], rol_enum))
            return usuarios
        except Exception as e:
            print("Error al obtener usuarios:", e)
            return usuarios
        finally:
            cerrar_conexion(conexion, cursor)

    @staticmethod
    def iniciar_sesion(usuario_input: str, clave_input: str) -> Usuario | None:
        usuario = UsuarioDAO.obtener_por_usuario(usuario_input)
        if usuario and usuario.verificar_credenciales(usuario_input, clave_input):
            return usuario
        return None

    @staticmethod
    def actualizar_rol(id_usuario: int, nuevo_rol: Rol) -> bool:
        conexion = obtener_conexion()
        if conexion is None:
            return False

        cursor = None
        try:
            cursor = conexion.cursor()
            sql = "UPDATE usuarios SET rol = %s WHERE id_usuario = %s"
            cursor.execute(sql, (nuevo_rol.value, id_usuario))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Error al actualizar rol del usuario:", e)
            return False
        finally:
            cerrar_conexion(conexion, cursor)

    @staticmethod
    def obtener_por_usuario(usuario: str) -> Usuario | None:
        conexion = obtener_conexion()
        if conexion is None:
            return None

        cursor = None
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT * FROM usuarios WHERE usuario = %s"
            cursor.execute(sql, (usuario,))
            resultado = cursor.fetchone()
            if resultado:
                rol_enum = Rol(resultado['rol'])
                return Usuario(resultado['id_usuario'], resultado['nombre'], resultado['usuario'], resultado['clave'], rol_enum)
            return None
        finally:
            cerrar_conexion(conexion, cursor)
