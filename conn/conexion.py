import mysql.connector
from mysql.connector import Error


def obtener_conexion():
    """
    Devuelve un objeto de conexión a la base de datos MySQL.
    """
    try:
        conexion = mysql.connector.connect(
            # Usuario el usuaio de MySQL y la clave segun su base de datos
            host="localhost",         
            user="root",        
            password="123456",  
            database="smart_home"      
        )
        return conexion
    except Error as e:
        print("Error al conectar con MySQL:", e)
        return None


def cerrar_conexion(conexion):
    """
    Cierra la conexión a MySQL si está abierta.
    """
    if conexion and conexion.is_connected():
        conexion.close()
