from database import crear_conexion

def ver_producto():
    conexion = crear_conexion()
    if not conexion:
        return []
    
    cursor = conexion.cursor()
    # Usando los nombres reales de tus columnas
    cursor.execute("SELECT id_producto, nombre_producto, stock, proveedor, precio, status, marca, descripcion FROM productos")
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def agregar_productos(nombre_producto, stock, proveedor, precio, status, marca, descripcion):
    conexion = crear_conexion()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre_producto, stock, proveedor, precio, status, marca, descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                      (nombre_producto, stock, proveedor, precio, status, marca, descripcion))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al agregar un producto. Tipo de error {e}")
        return False

def actualizar_productos(id_producto, new_nombre_producto, new_stock, new_proveedor, new_precio, new_status, new_marca, new_descripcion):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET nombre_producto = %s, stock = %s, proveedor = %s, precio = %s, status = %s, marca = %s, descripcion = %s WHERE id_producto = %s", 
                      (new_nombre_producto, new_stock, new_proveedor, new_precio, new_status, new_marca, new_descripcion, id_producto))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al actualizar productos. Tipo de error: {e}")
        return False

def eliminar_producto(id_producto):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al eliminar producto. Tipo de error: {e}")
        return False