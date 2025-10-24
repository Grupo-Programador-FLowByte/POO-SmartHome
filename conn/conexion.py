import mysql.connector
from mysql.connector import errorcode

def obtener_conexion():
    """
    Devuelve un objeto de conexión a la base de datos MySQL.
    """
    try:
        conexion = mysql.connector.connect(
            # Usuario el usuaio de MySQL y la clave segun su base de datos
            user="root",        
            password="123456",
            host="localhost",   
            database="smart_home",
            port = "3306"      
        )
        return conexion
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
             print("Usuario o Password no válido") 
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe.")
        else:
            print("Se ha producido un error. Por favor contacte al admin.")
        return None


def cerrar_conexion(conexion):
    """
    Cierra la conexión a MySQL si está abierta.
    """
    if conexion and conexion.is_connected():
        conexion.close()
