from dispositivos import listar_dispositivos, eliminar_dispositivos, agregar_dispositivo, buscar_dispositivos
from automatizacion import activar_modo_ahorro, reglas_de_automatizacion
from lista_dispositivos import *
from usuarios import cambiar_rol_usuario, registrar_usuario, iniciar_sesion, obtener_usuario_por_nombre
from utils import imprimir_valores
from claves import claves_usuarios
import json
import os


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


def gestionar_dispositivos():
    while True:
        mostrar_menu_dispositivos()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print("Funcion agregar dispositivos")
            agregar_dispositivo(dispositivos)
        elif opcion == "2":
            print("Funcion listar dispositivos\n")
            listar_dispositivos(dispositivos)
        elif opcion == "3":
            print("Funcion buscar dispositivo")
            buscar_dispositivos(dispositivos)
        elif opcion == "4":
            print("Funcion eliminar dispositivo")
            eliminar = input("¿Desea eliminar un dispositivo? (SI/NO): ")
            if eliminar.lower() == "si":
                try:
                    id_a_eliminar = int(
                        input("Ingrese el ID del dispositivo a eliminar: "))
                    resultado = eliminar_dispositivos(
                        dispositivos, eliminar, id_a_eliminar)
                    if resultado:
                        print("Dispositivo eliminado correctamente.")
                    else:
                        print("No se encontró el dispositivo.")
                except:
                    print("ERROR, el dato a ingresar debe ser numérico")
            else:
                print("No se elimina ningún dispositivo.")
        elif opcion == "5":
            gestion_administrador()
            break
        else:
            print("Opcion inorrecta")


def gestionar_automatizacion():
    while True:
        mostrar_menu_automatizaciones()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print("Funcion modo ahorro de energia")
            activar_modo_ahorro(dispositivos)

        elif opcion == "2":
            print("Reglas de automatización")
            reglas_de_automatizacion(dispositivos)

        elif opcion == "3":
            gestion_administrador()
        else:
            print("Opcion inorrecta")


def gestion_administrador():
    while True:
        mostrar_menu_admin()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            gestionar_dispositivos()
        elif opcion == "2":
            gestionar_automatizacion()
        elif opcion == "3":
            try:
                with open("usuarios.json", "r") as f:
                    usuarios = json.load(f)
                print("\n--- LISTA DE USUARIOS ---")
                for i, u in enumerate(usuarios):
                    print(f"{i+1}. {u['usuario']} ({u['rol']})")
                num = input(
                    "Ingrese el número de usuario para cambiar el rol: ")
                if num.isdigit():
                    resultado = cambiar_rol_usuario(int(num))
                    if resultado:
                        print("Rol cambiado correctamente.")
                    else:
                        print("Opción inválida.")
                else:
                    print("Opción inválida.")
            except Exception as e:
                print("Error al acceder a los usuarios:", e)
        elif opcion == "4":
            print("Se cerro sesión")
            menu()
        else:
            print("Opcion inorrecta")


def gestion_estandar(usuario):
    while True:
        mostrar_menu_estandar()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            datos_usuario = obtener_usuario_por_nombre(
                usuario, 'usuario', None)
            print("\n--- DATOS PERSONALES ---")
            imprimir_valores(datos_usuario, claves_usuarios)
        elif opcion == "2":
            activar_modo_ahorro(dispositivos)
        elif opcion == "3":
            listar_dispositivos(dispositivos)
        elif opcion == "4":
            print("Se cerro sesión")
            menu()
        else:
            print("Opcion inorrecta")


def menu():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            print("=== REGISTRO DE USUARIO ===")

            archivo = "usuarios.json"
            usuarios = json.load(
                open(archivo)) if os.path.exists(archivo) else []

            nombre = input("Nombre completo: ")
            usuario = input("Nombre de usuario: ")
            clave = input("Contraseña: ")

            if not usuarios:
                rol = "admin"
                print("Primer usuario → asignado como ADMIN.")
            else:
                rol = "admin" if input(
                    "¿Rol admin? (s/n): ").lower() == "s" else "estandar"

            registrar_usuario(nombre, usuario, clave, rol)
            print(f"Usuario '{usuario}' registrado como {rol.upper()}.")
        elif opcion == "2":
            usuario = input("Nombre de usuario: ")
            clave = input("Contraseña: ")
            sesion = iniciar_sesion(usuario, clave)
            if sesion:
                print(
                    f"Bienvenido, {sesion['nombre']} ({sesion['rol'].upper()})")
                if sesion["rol"] == "admin":
                    gestion_administrador()
                else:
                    gestion_estandar(usuario)
            else:
                print("Usuario o contraseña incorrectos.")
        elif opcion == "3":
            break
        else:
            print("Opcion incorrecta")


if __name__ == "__main__":
    menu()
