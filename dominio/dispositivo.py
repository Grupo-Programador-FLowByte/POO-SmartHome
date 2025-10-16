
"""
Tareas de Franco

Objetivo: Crear el módulo `dispositivo_dao.py` que maneje todas las operaciones de dispositivos en la aplicación, usando la lista de objetos `Dispositivo` o conectándose a MySQL más adelante.

Tareas específicas:
1. Crear `dispositivo_dao.py` con la clase `DispositivoDAO`.
2. Implementar los métodos CRUD para dispositivos:
    - insertar(nombre, tipo, estado, usuario: Usuario) → agrega un dispositivo y devuelve el objeto creado.
    - obtener_todos() → devuelve la lista de todos los dispositivos.
    - obtener_por_id(id_dispositivo) → devuelve un dispositivo según su ID.
    - obtener_por_usuario(id_usuario) → devuelve todos los dispositivos de un usuario.
    - eliminar(id_dispositivo) → elimina un dispositivo por su ID y devuelve True/False según éxito.
3. Probar que se puedan listar, buscar, agregar y eliminar dispositivos usando los métodos del DAO.
4. Integrar el DAO con el `main.py` para que todas las operaciones de dispositivos funcionen desde los menús.
5. Opcional: Preparar la conexión a MySQL (`conn/conexion.py`) y modificar los métodos de DAO para que interactúen con la base de datos.

Ejemplo de estructura de `dispositivo_dao.py`:

from conn.conexion import obtener_conexion
from dominio.dispositivo import Dispositivo

class DispositivoDAO:

    dispositivos = []  # lista temporal, luego se puede cambiar a MySQL

    @staticmethod
    def insertar(nombre, tipo, estado, usuario):
        disp = Dispositivo(nombre, tipo, estado, usuario)
        DispositivoDAO.dispositivos.append(disp)
        return disp

    @staticmethod
    def obtener_todos():
        return DispositivoDAO.dispositivos

    @staticmethod
    def obtener_por_id(id_dispositivo):
        for d in DispositivoDAO.dispositivos:
            if d.id_dispositivo == id_dispositivo:
                return d
        return None

    @staticmethod
    def obtener_por_usuario(id_usuario):
        return [d for d in DispositivoDAO.dispositivos if d.usuario.id_usuario == id_usuario]

    @staticmethod
    def eliminar(id_dispositivo):
        disp = DispositivoDAO.obtener_por_id(id_dispositivo)
        if disp:
            DispositivoDAO.dispositivos.remove(disp)
            return True
        return False

Resultado esperado:
- Poder usar el DAO desde `main.py` para que las opciones de agregar, listar, buscar y eliminar dispositivos funcionen correctamente.
- Flujo totalmente funcional sin errores.
- Luego se puede reemplazar la lista temporal por conexión a MySQL para persistencia.
"""

from usuario import Usuario

class Dispositivo:
    def __init__(self, id_dispositivo, nombre, tipo, estado):
        self.__id_dispositivo = id_dispositivo
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado

    @property
    def id_dispositivo(self):
        return self.__id_dispositivo

    def __str__(self):
        return f"Dispositivo(ID: {self.id_dispositivo}, Nombre: {self.nombre}, Tipo: {self.tipo}, Estado: {self.estado})"
