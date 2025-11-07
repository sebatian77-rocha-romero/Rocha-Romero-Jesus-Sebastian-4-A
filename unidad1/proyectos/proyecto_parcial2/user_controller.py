from database import *

def ver_usuarios():
    conn = crear_conexion()
    
    if not conn:
        return []
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT ID, username FROM usuarios")
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"error al obtener usuarios: {e}")
        return []
    finally:
        if conn and conn.is_connected():
            conn.close()

def agregar_usuarios(username, password):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            # CORREGIDO: usar 'username' en lugar de 'usuario'
            consulta = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
            cursor.execute(consulta, (username, password))
            conexion.commit()
            return True
        except Error as e:
            print(f"Error al crear un usuario. Tipo de error {e}")
            return False
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()


def actualizar_usuarios(user_id, username, password=None):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            if password:
                consulta = "UPDATE usuarios SET username = %s, password = %s WHERE id = %s"
                cursor.execute(consulta, (username, password, user_id))
            else:
                consulta = "UPDATE usuarios SET username = %s WHERE id = %s"
                cursor.execute(consulta, (username, user_id))
            
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar usuario. Tipo de error: {e}")
            return False
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def eliminar_usuario(user_id):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(consulta, (user_id,))
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error al eliminar el usuario. Tipo de error: {e}")
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
