from enum import Enum


def mostrar_atributos(objeto, claves=None):
    """
    Imprime los atributos de un objeto o diccionario de forma legible.
    Maneja atributos privados y Enum.
    """
    if isinstance(objeto, dict):
        items = objeto.items()
    else:
        # Tomamos los atributos del objeto con vars y propiedades
        items = {}
        for attr in dir(objeto):
            if attr.startswith("_") and not attr.startswith("__class__") and not attr.startswith("__module__"):
                # ignoramos métodos y atributos especiales
                continue
            if callable(getattr(objeto, attr)):
                continue
            valor = getattr(objeto, attr)
            # Convertir Enum a su valor
            if isinstance(valor, Enum):
                valor = valor.value
            items[attr] = valor

        items = items.items()

    for k, v in items:
        if not claves or k in claves:
            print(f"{k}: {v}")
    print("-" * 40)

# utils/utilidades.py


def mostrar_dispositivos(dispositivos):
    """
    Muestra los dispositivos de forma clara y visual en consola.
    """
    if not dispositivos:
        print("No hay dispositivos para mostrar.\n")
        return

    print("\n--- Dispositivos Registrados ---\n")
    for d in dispositivos:
        print(f"ID     : {d.id_dispositivo}")
        print(f"Nombre : {d.nombre}")
        print(f"Tipo   : {d.tipo}")
        print(f"Estado : {'Encendido' if d.estado else 'Apagado'}")
        print("-" * 30)  # separador
    print()  # línea vacía al final


def mostrar_automatizaciones(automatizaciones):
    if not automatizaciones:
        print("No hay automatizaciones para mostrar.\n")
        return

    print("\n--- Automatizaciones Registradas ---\n")
    for a in automatizaciones:
        print(f"ID           : {a.id_automatizacion}")
        print(f"Nombre       : {a.nombre}")
        print(f"Funcionalidad: {a.funcionalidad}")
        print(f"Estado       : {'Activo' if a.estado else 'Inactivo'}")
        print("-" * 40)
    print()
