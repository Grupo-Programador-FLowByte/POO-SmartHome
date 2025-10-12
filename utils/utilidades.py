def mostrar_atributos(objeto, claves=None):
    """
    Imprime los atributos de un objeto o diccionario.
    Si se pasa 'claves', solo imprime esas claves.
    """
    if isinstance(objeto, dict):
        items = objeto.items()
    else:
        items = vars(objeto).items()  # toma solo atributos de instancia

    for k, v in items:
        if not claves or k in claves:
            print(f"{k}: {v}")
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
