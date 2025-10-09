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

