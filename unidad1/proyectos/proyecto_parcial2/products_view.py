import tkinter as tk
from tkinter import messagebox, ttk
from product_controller import ver_producto, agregar_productos, actualizar_productos, eliminar_producto
from user_view import UserApp

class UserApp2:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Bienvenido {username}")
        self.root.geometry("900x700")
        self.root.resizable(True, True)        
        
        self.crear_elementos()
        self.ver_productos()
        self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root, text=f"Hola, {self.username}", font=("Comic Sans MS", 22, "bold")).pack(pady=10)
        tk.Button(self.root, text="Cerrar sesión", width=15, command=self.cerrar_sesion).pack(pady=20, padx=10)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar productos", width=20, command=self.agregar_producto).pack(pady=5)
        tk.Button(frame_botones, text="Actualizar productos", width=20, command=self.actualizar_producto).pack(pady=5)
        tk.Button(frame_botones, text="Eliminar productos", width=20, command=self.eliminar_producto).pack(pady=5)
        tk.Button(frame_botones, text="Ver usuarios", width=20, command=self.abrir_user_view).pack(pady=5)

        tk.Label(self.root, text="Lista de productos", font=("Arial", 16, "bold")).pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("id", "nombre", "stock", "proveedor", "precio", "status", "marca", "descripcion"), show="headings", height=10)
        
        # Encabezados
        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("stock", text="Stock")
        self.tree.heading("proveedor", text="Proveedor")
        self.tree.heading("precio", text="Precio")
        self.tree.heading("status", text="Status")
        self.tree.heading("marca", text="Marca")
        self.tree.heading("descripcion", text="Descripción")

        # Columnas
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("nombre", width=120, anchor="center")
        self.tree.column("stock", width=80, anchor="center")
        self.tree.column("proveedor", width=120, anchor="center")
        self.tree.column("precio", width=80, anchor="center")
        self.tree.column("status", width=80, anchor="center")
        self.tree.column("marca", width=100, anchor="center")
        self.tree.column("descripcion", width=150, anchor="center")
        
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

    def ver_productos(self):
        # Limpiar tabla
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # Obtener productos
        productos = ver_producto()
        print(f"DEBUG: Productos obtenidos: {productos}")
        
        # Insertar en la tabla
        for producto in productos:
            self.tree.insert("", tk.END, values=producto)

    def agregar_producto(self):
        def guardar():
            nombre = entry_nombre.get().strip()
            stock = entry_stock.get().strip()
            proveedor = entry_proveedor.get().strip()
            precio = entry_precio.get().strip()
            status = entry_status.get().strip()
            marca = entry_marca.get().strip()
            descripcion = entry_desc.get().strip()

            if not nombre or not stock or not proveedor or not precio:
                messagebox.showwarning("Campos vacíos", "Complete todos los campos obligatorios.")
                return

            if agregar_productos(nombre, stock, proveedor, precio, status, marca, descripcion):
                messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente.")
                self.ver_productos()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo agregar el producto.")
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Producto")
        ventana.geometry("300x400")
        ventana.transient(self.root)
        ventana.grab_set()
        
        tk.Label(ventana, text="Nombre del producto").pack(pady=5)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.pack(pady=5)
        
        tk.Label(ventana, text="Stock").pack(pady=5)
        entry_stock = tk.Entry(ventana)
        entry_stock.pack(pady=5)
        
        tk.Label(ventana, text="Proveedor").pack(pady=5)
        entry_proveedor = tk.Entry(ventana)
        entry_proveedor.pack(pady=5)
        
        tk.Label(ventana, text="Precio").pack(pady=5)
        entry_precio = tk.Entry(ventana)
        entry_precio.pack(pady=5)
        
        tk.Label(ventana, text="Status").pack(pady=5)
        entry_status = tk.Entry(ventana)
        entry_status.pack(pady=5)
        
        tk.Label(ventana, text="Marca").pack(pady=5)
        entry_marca = tk.Entry(ventana)
        entry_marca.pack(pady=5)
        
        tk.Label(ventana, text="Descripción").pack(pady=5)
        entry_desc = tk.Entry(ventana)
        entry_desc.pack(pady=5)
        
        tk.Button(ventana, text="Crear producto", command=guardar).pack(pady=10)

    def actualizar_producto(self):
        seleccionado = self.tree.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto de la lista.")
            return

        valores = self.tree.item(seleccionado, "values")
        id_producto = valores[0]  
        nombre_actual = valores[1]  

        def guardar():
            nuevo_nombre = entry_nombre.get().strip()
            nuevo_stock = entry_stock.get().strip()
            nuevo_proveedor = entry_proveedor.get().strip()
            nuevo_precio = entry_precio.get().strip()
            nuevo_status = entry_status.get().strip()
            nueva_marca = entry_marca.get().strip()
            nueva_desc = entry_desc.get().strip()

            if not nuevo_nombre:
                messagebox.showwarning("Campos vacíos", "Ingrese al menos el nombre del producto.")
                return

            if actualizar_productos(id_producto, nuevo_nombre, nuevo_stock, nuevo_proveedor, nuevo_precio, nuevo_status, nueva_marca, nueva_desc):
                messagebox.showinfo("Éxito", f"Producto '{nuevo_nombre}' actualizado correctamente.")
                self.ver_productos()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el producto.")

        ventana = tk.Toplevel(self.root)
        ventana.title("Actualizar Producto")
        ventana.geometry("300x400")
        ventana.transient(self.root)
        ventana.grab_set()
        
        tk.Label(ventana, text="Nuevo nombre").pack(pady=5)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.insert(0, nombre_actual)
        entry_nombre.pack(pady=5)
        
        tk.Label(ventana, text="Nuevo stock").pack(pady=5)
        entry_stock = tk.Entry(ventana)
        entry_stock.pack(pady=5)
        
        tk.Label(ventana, text="Nuevo proveedor").pack(pady=5)
        entry_proveedor = tk.Entry(ventana)
        entry_proveedor.pack(pady=5)
        
        tk.Label(ventana, text="Nuevo precio").pack(pady=5)
        entry_precio = tk.Entry(ventana)
        entry_precio.pack(pady=5)
        
        tk.Label(ventana, text="Nuevo status").pack(pady=5)
        entry_status = tk.Entry(ventana)
        entry_status.pack(pady=5)
        
        tk.Label(ventana, text="Nueva marca").pack(pady=5)
        entry_marca = tk.Entry(ventana)
        entry_marca.pack(pady=5)
        
        tk.Label(ventana, text="Nueva descripción").pack(pady=5)
        entry_desc = tk.Entry(ventana)
        entry_desc.pack(pady=5)
        
        tk.Button(ventana, text="Guardar cambios", command=guardar).pack(pady=10)

    def eliminar_producto(self):
        seleccionado = self.tree.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar.")
            return

        valores = self.tree.item(seleccionado, "values")
        id_producto = valores[0]  
        nombre_producto = valores[1]  

        confirmar = messagebox.askyesno("Confirmar", f"¿Desea eliminar el producto '{nombre_producto}'?")
        if confirmar:
            if eliminar_producto(id_producto):
                messagebox.showinfo("Eliminado", f"Producto '{nombre_producto}' eliminado correctamente.")
                self.ver_productos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def abrir_user_view(self):
        try:
            # Abre la ventana de usuarios directamente
            UserApp(self.username)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir gestión de usuarios:\n{e}")

    def cerrar_sesion(self):
        self.root.destroy()

if __name__ == "__main__":
    app2 = UserApp2("admin")