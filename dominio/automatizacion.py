"""
Tareas de Valentino

Objetivo: Crear el módulo `automatizacion_dao.py` que maneje todas las operaciones de automatizaciones en la aplicación, permitiendo activar/desactivar modos y listar reglas.

Tareas específicas:
1. Crear `automatizacion_dao.py` con la clase `AutomatizacionDAO`.
2. Implementar los métodos CRUD para automatizaciones:
    - insertar(nombre, funcionalidad, estado=False) → agrega una automatización y devuelve el objeto creado.
    - obtener_todos() → devuelve la lista de todas las automatizaciones.
    - obtener_por_id(id_automatizacion) → devuelve una automatización según su ID.
    - activar_modo(id_automatizacion) → cambia el estado de la automatización (activa/desactiva).
    - eliminar(id_automatizacion) → elimina una automatización por su ID y devuelve True/False según éxito.
3. Probar que se puedan listar, activar y mostrar reglas de automatización usando los métodos del DAO.
4. Integrar el DAO con el `main.py` para que todas las operaciones de automatización funcionen desde los menús.
5. Opcional: Preparar la conexión a MySQL (`conn/conexion.py`) y modificar los métodos de DAO para que interactúen con la base de datos.

Ejemplo de estructura de `automatizacion_dao.py`:

from dominio.automatizacion import Automatizacion

class AutomatizacionDAO:

    automatizaciones = []  # lista temporal, luego se puede cambiar a MySQL

    @staticmethod
    def insertar(nombre, funcionalidad, estado=False):
        auto = Automatizacion(len(AutomatizacionDAO.automatizaciones)+1, nombre, funcionalidad, estado)
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

Resultado esperado:
- Poder usar el DAO desde `main.py` para que las opciones de activar modos y mostrar reglas funcionen correctamente.
- Flujo totalmente funcional sin errores.
- Luego se puede reemplazar la lista temporal por conexión a MySQL para persistencia.
"""

class Automatizacion:
    def __init__(self, id_automatizacion, nombre, funcionalidad, estado=False):
        self.__id_automatizacion = id_automatizacion
        self.nombre = nombre
        self.funcionalidad = funcionalidad
        self.estado = estado  # False = Inactivo, True = Activo

    @property
    def id_automatizacion(self):
        return self.__id_automatizacion

    @id_automatizacion.setter
    def id_automatizacion(self, id_automatizacion):
        self.__id_automatizacion = id_automatizacion

    def activar_modo(self):
        """Cambia el estado de la automatización."""
        self.estado = not self.estado

<<<<<<< HEAD
    def reglas_de_automatizacion(self):
        """Devuelve una descripción de las reglas de la automatización."""
        return f"Reglas de {self.nombre}: {self.funcionalidad}"
    

=======
    def __str__(self):
        return (f"Automatizacion:\n"
                f"  {self.nombre} ({self.id_automatizacion})\n"
                f"  Funcionalidad: {self.funcionalidad}\n"
                f"  Estado: {'Activo' if self.estado else 'Inactivo'}\n")
>>>>>>> main
