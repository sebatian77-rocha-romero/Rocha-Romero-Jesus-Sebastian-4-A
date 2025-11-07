#controlador encargado de la logica de autenticasion.
#nos sirve para separar la login¡ca del login para mantener limpio el codigo de la interfaz

from database import crear_conexion
import mysql.connector
from mysql.connector import Error

def validar_credenciales(usuario, password):
    conn = crear_conexion()  # Solo recibe la conexión, no tupla
    
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM usuarios WHERE username=%s AND password=%s"
        cursor.execute(sql, (usuario, password))
        result = cursor.fetchone()
        
        return bool(result)
    except Exception as e:
        print(f"Error en la consulta: {e}")
        return False
    finally:
        if conn and conn.is_connected():
            conn.close()

