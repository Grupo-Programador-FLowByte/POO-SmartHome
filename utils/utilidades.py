from enum import Enum


def mostrar_atributos(objeto, claves=None):
    """
    Muestra atributos de un objeto o diccionario de manera ordenada.
    Ignora atributos internos y name-mangled.
    """
    if isinstance(objeto, dict):
        items = objeto.items()
    else:
        items = {}
        for attr in vars(objeto):
            # Ignorar atributos internos que empiezan con doble guion bajo (name-mangling)
            # Solo tus atributos privados
            if attr.startswith("_") and not attr.startswith("_Usuario__"):
                continue
            valor = getattr(objeto, attr)
            if isinstance(valor, Enum):
                valor = valor.value
            # Limpiar el nombre si es name-mangled
            if attr.startswith(f"_{objeto.__class__.__name__}__"):
                attr = attr[len(f"_{objeto.__class__.__name__}__"):]
            items[attr] = valor
        items = items.items()

    for k, v in items:
        if not claves or k in claves:
            print(f"{k}: {v}")
    print("-" * 40)


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
