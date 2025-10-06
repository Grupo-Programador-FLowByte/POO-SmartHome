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
