from conn.conexion import obtener_conexion
from dominio.usuario import Usuario


class UsuarioDAO:

    @staticmethod
    def insertar(nombre: str, usuario: str, clave: str, rol: str) -> Usuario:
        """
        Inserta un nuevo usuario en la base de datos y devuelve el objeto Usuario creado.
        """
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios (nombre, usuario, clave, rol) VALUES (%s, %s, %s, %s)"
        valores = (nombre, usuario, clave, rol)
        cursor.execute(sql, valores)
        conexion.commit()
        id_usuario = cursor.lastrowid
        conexion.close()
        return Usuario(id_usuario, nombre, usuario, clave, rol)

    @staticmethod
    def obtener_todos() -> list[Usuario]:
        """
        Devuelve una lista con todos los usuarios de la base de datos.
        """
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        conexion.close()
        return [Usuario(r['id_usuario'], r['nombre'], r['usuario'], r['clave'], r['rol']) for r in resultados]

    @staticmethod
    def obtener_por_usuario(usuario: str) -> Usuario | None:
        """
        Devuelve un usuario según su nombre de usuario, o None si no existe.
        """
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        sql = "SELECT * FROM usuarios WHERE usuario = %s"
        cursor.execute(sql, (usuario,))
        resultado = cursor.fetchone()
        conexion.close()
        if resultado:
            return Usuario(resultado['id_usuario'], resultado['nombre'], resultado['usuario'], resultado['clave'], resultado['rol'])
        return None

    @staticmethod
    def iniciar_sesion(usuario_input: str, clave_input: str) -> Usuario | None:
        """
        Devuelve el usuario si las credenciales coinciden.
        """
        usuario = UsuarioDAO.obtener_por_usuario(usuario_input)
        if usuario and usuario.verificar_credenciales(usuario_input, clave_input):
            return usuario
        return None

    @staticmethod
    def actualizar_rol(id_usuario: int, nuevo_rol: str) -> bool:
        """
        Actualiza el rol de un usuario según su ID. Devuelve True si se actualizó.
        """
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "UPDATE usuarios SET rol = %s WHERE id_usuario = %s"
        cursor.execute(sql, (nuevo_rol, id_usuario))
        conexion.commit()
        actualizado = cursor.rowcount > 0
        conexion.close()
        return actualizado
