import mysql.connector
from mysql.connector import Error

'''''''''
def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='base de usuarios'
        )

        if conexion.is_connected():
            print("Conexión MySQL exitosa")
            return conexion
    
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    conn = crear_conexion()
    if conn:
        # Do something with the connection
        conn.close()
        print("Conexión cerrada")
    
'''''''''

def crear_conexion():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="proyect_p2"
        )
        if conexion.is_connected():
            print("Conexion MySQL exitosa")
            return conexion
    except Error as e:
        print(f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ..{e}") 

