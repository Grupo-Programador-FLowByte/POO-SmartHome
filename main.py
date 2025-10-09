from dominio.usuario import Usuario
# from dominio.dispositivo import Dispositivo
# from dominio.automatizacion import Automatizacion

from dao.usuario_dao import UsuarioDAO
# from dao.dispositivo_dao import DispositivoDAO
from dao.automatizacion_dao import AutomatizacionDAO

from utils.utilidades import mostrar_atributos

# ------------------ Menús ------------------


def mostrar_menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Salir")


def mostrar_menu_admin():
    print("\n--- MENÚ USUARIO ADMIN ---")
    print("1. Gestión de dispositivos")
    print("2. Automatizaciones")
    print("3. Modificar rol de usuario")
    print("4. Cerrar sesión")


def mostrar_menu_estandar():
    print("\n--- MENÚ USUARIO ESTÁNDAR ---")
    print("1. Consultar datos personales")
    print("2. Activar modo ahorro de energía")
    print("3. Mostrar dispositivos")
    print("4. Cerrar sesión")


def mostrar_menu_dispositivos():
    print("\n--- GESTIÓN DE DISPOSITIVOS ---")
    print("1. Agregar dispositivo")
    print("2. Listar dispositivos")
    print("3. Buscar dispositivo")
    print("4. Eliminar dispositivo")
    print("5. Volver al menú")


def mostrar_menu_automatizaciones():
    print("\n--- AUTOMATIZACIONES DISPONIBLES ---")
    print("1. Activar modo ahorro de energía")
    print("2. Ver reglas de automatización")
    print("3. Volver al menú")

# ------------------ Gestión de Dispositivos ------------------


def gestionar_dispositivos():
    while True:
        mostrar_menu_dispositivos()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del dispositivo: ")
            tipo = input("Tipo: ")
            estado = input("Estado (True/False): ").lower() == "true"
            usuario_id = int(input("ID de usuario propietario: "))
            DispositivoDAO.insertar(nombre, tipo, estado, usuario_id)
            print("Dispositivo agregado.")
        elif opcion == "2":
            dispositivos = DispositivoDAO.obtener_todos()
            for d in dispositivos:
                mostrar_atributos(d)
        elif opcion == "3":
            id_disp = int(input("ID del dispositivo a buscar: "))
            disp = DispositivoDAO.obtener_por_id(id_disp)
            if disp:
                mostrar_atributos(disp)
            else:
                print("Dispositivo no encontrado.")
        elif opcion == "4":
            id_disp = int(input("ID del dispositivo a eliminar: "))
            if DispositivoDAO.eliminar(id_disp):
                print("Dispositivo eliminado.")
            else:
                print("No se encontró el dispositivo.")
        elif opcion == "5":
            break
        else:
            print("Opción incorrecta.")

# ------------------ Gestión de Automatizaciones ------------------


def gestionar_automatizacion():
    while True:
        mostrar_menu_automatizaciones()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_auto = int(input("ID de la automatización a activar: "))
            AutomatizacionDAO.activar_modo(id_auto)
            print("Modo activado/desactivado según estado actual.")
        elif opcion == "2":
            autos = AutomatizacionDAO.obtener_todos()
            for a in autos:
                mostrar_atributos(a)
        elif opcion == "3":
            break
        else:
            print("Opción incorrecta.")

# ------------------ Gestión Usuarios ------------------


def gestion_administrador():
    while True:
        mostrar_menu_admin()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_dispositivos()
        elif opcion == "2":
            gestionar_automatizacion()
        elif opcion == "3":
            usuarios = UsuarioDAO.obtener_todos()
            for u in usuarios:
                mostrar_atributos(u)

            try:
                id_usuario = int(
                    input("Ingrese ID del usuario para cambiar rol: "))
                nuevo_rol = input("Nuevo rol (admin/estandar): ").lower()

                if nuevo_rol not in ["admin", "estandar"]:
                    print(
                        "Error: el rol debe ser 'admin' o 'estandar'. No se realizó ningún cambio.")
                    continue

                if UsuarioDAO.actualizar_rol(id_usuario, nuevo_rol):
                    print("Rol actualizado correctamente.")
                else:
                    print("No se encontró el usuario con ese ID.")

            except ValueError:
                print("Error: el ID debe ser un número.")
        elif opcion == "4":
            break
        else:
            print("Opción incorrecta.")


def gestion_estandar(usuario_obj):
    while True:
        mostrar_menu_estandar()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_atributos(usuario_obj)
        elif opcion == "2":
            print("Activando modo ahorro de energía para tus dispositivos...")
            # Aquí podés agregar lógica para activar modo ahorro
        elif opcion == "3":
            dispositivos = DispositivoDAO.obtener_por_usuario(
                usuario_obj.get_id_usuario())
            for d in dispositivos:
                mostrar_atributos(d)
        elif opcion == "4":
            break
        else:
            print("Opción incorrecta.")

# ------------------ Menú Principal ------------------


def menu():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre completo: ")
            usuario = input("Usuario: ")
            clave = input("Contraseña: ")
            rol = "admin" if input(
                "Rol admin? (s/n): ").lower() == "s" else "estandar"
            id_usuario = UsuarioDAO.insertar(nombre, usuario, clave, rol)
            print(f"Usuario '{usuario}' registrado con ID {id_usuario}.")
        elif opcion == "2":
            usuario = input("Usuario: ")
            clave = input("Contraseña: ")
            usuario_obj = UsuarioDAO.iniciar_sesion(usuario, clave)
            if usuario_obj:
                print(f"Bienvenido {usuario_obj.nombre} ({usuario_obj.rol})")
                if usuario_obj.rol == "admin":
                    gestion_administrador()
                else:
                    gestion_estandar(usuario_obj)
            else:
                print("Usuario o contraseña incorrectos.")
        elif opcion == "3":
            break
        else:
            print("Opción incorrecta.")

# ------------------ Inicio ------------------


if __name__ == "__main__":
    menu()
