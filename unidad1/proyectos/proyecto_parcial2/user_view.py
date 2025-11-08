import tkinter as tk
from tkinter import messagebox, ttk
from auth_controller import validar_credenciales
import user_controller as uc
from user_controller import ver_usuarios, agregar_usuarios, actualizar_usuarios, eliminar_usuario


class UserApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Bienvenido {username}")
        self.root.geometry("800x500")
        self.root.resizable(True, True)   

        self.tree = None     
        
        self.crear_elementos()
        self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root,text=f"hola {self.username}",font=("Comic Sans MS",22,"bold")).pack(pady=10)
        tk.Button(self.root,text="Ver usuarios", command=self.ver_usuarios ,width=20).pack(pady=10)
        tk.Button(self.root,text="Agregar usuarios", command=self.agregar_usuarios, width=20).pack(pady=10)
        tk.Button(self.root,text="Actualizar usuarios", command=self.actualizar_usuarios, width=20).pack(pady=10)
        tk.Button(self.root,text="Eliminar usuarios", command=self.eliminar_usuarios , width=20).pack(pady=10)
        tk.Button(self.root,text="Cerrar sesión", width=50,command=self.cerrar_sesion).pack(pady=20)
        
        #Creacion de las tablas para ver usuarios
        self.tree=ttk.Treeview(self.root, columns=("ID","Username"),height=10,show="headings")
        self.tree.heading("ID",text="ID usuario")
        self.tree.heading("Username",text="Nombre del usuario")
        self.tree.pack(padx=10,pady=9,fill="both",expand=True)
        for (us_nomb,ID_us) in uc.ver_usuarios():
            self.tree.insert('',0,text="",values=(us_nomb,ID_us))

    '''''        
    def ver_usuarios(self):
        #Creacion de tablas para ver usuarios
        self.tree=ttk.Treeview(self.root, columns=("ID","Username"),height=10,show="headings")
        self.tree.heading("ID",text="ID usuario")
        self.tree.heading("Username",text="Nombre del usuario")
        self.tree.pack(padx=10,pady=9,fill="both",expand=True)
        for (us_nomb,ID_us) in uc.ver_usuarios():
            self.tree.insert('',0,text="",values=(us_nomb,ID_us))
    '''              

    #ver usuariso en la base de datos
    def ver_usuarios(self):
        if not self.tree:
            return
            
        # Limpiar tabla existente
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            usuarios = uc.ver_usuarios() 
            # Insertar usuarios en la tabla
            for usuario in usuarios:
                self.tree.insert('', 'end', values=usuario)
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar usuarios: {str(e)}")

    def agregar_usuarios(self):
        # Crear ventana emergente para agregar usuario
        agregar_window = tk.Toplevel(self.root)
        agregar_window.title("Agregar Usuario")
        agregar_window.geometry("300x200")
        agregar_window.resizable(False, False)
        
        # Centrar ventana
        agregar_window.transient(self.root)
        agregar_window.grab_set()
        
        # Campos del formulario
        tk.Label(agregar_window, text="Nombre de usuario:").pack(pady=5)
        username_entry = tk.Entry(agregar_window, width=30)
        username_entry.pack(pady=5)
        
        tk.Label(agregar_window, text="Contraseña:").pack(pady=5)
        password_entry = tk.Entry(agregar_window, width=30, show="*")
        password_entry.pack(pady=5)
        
        def guardar_usuario():
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            
            if not username or not password:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            
            try:
                # función del controlador para agregar usuario
                resultado = agregar_usuarios(username, password)
                if resultado:
                    messagebox.showinfo("Éxito", "Usuario agregado correctamente")
                    agregar_window.destroy()
                    self.ver_usuarios()  
                else:
                    messagebox.showerror("Error", "No se pudo agregar el usuario")
            except Exception as e:
                messagebox.showerror("Error", f"Error al agregar usuario: {str(e)}")
        
        # Botones
        tk.Button(agregar_window, text="Guardar", command=guardar_usuario).pack(pady=10)
        tk.Button(agregar_window, text="Cancelar", command=agregar_window.destroy).pack(pady=5)

    def actualizar_usuarios(self):
        # Verificar si hay un usuario seleccionado
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione un usuario para actualizar")
            return
        
        # Obtener datos del usuario seleccionado
        item = self.tree.item(seleccion[0])
        user_id, old_username = item['values']
        
        # Creasion de la ventana emergente para actualizar usuario
        actualizar_window = tk.Toplevel(self.root)
        actualizar_window.title("Actualizar Usuario")
        actualizar_window.geometry("300x250")
        actualizar_window.resizable(False, False)
        
        actualizar_window.transient(self.root)
        actualizar_window.grab_set()
        
        # Campos formulario
        tk.Label(actualizar_window, text="ID Usuario:").pack(pady=5)
        id_label = tk.Label(actualizar_window, text=str(user_id))
        id_label.pack(pady=5)
        
        tk.Label(actualizar_window, text="Nuevo nombre de usuario:").pack(pady=5)
        username_entry = tk.Entry(actualizar_window, width=30)
        username_entry.insert(0, old_username)
        username_entry.pack(pady=5)
        
        tk.Label(actualizar_window, text="Nueva contraseña (dejar vacío para no cambiar):").pack(pady=5)
        password_entry = tk.Entry(actualizar_window, width=30, show="*")
        password_entry.pack(pady=5)
        
        def guardar_cambios():
            new_username = username_entry.get().strip()
            new_password = password_entry.get().strip()
            
            if not new_username:
                messagebox.showerror("Error", "El nombre de usuario es obligatorio")
                return
            
            try:
                # Llamar a la función del controlador para actualizar usuario
                resultado = actualizar_usuarios(user_id, new_username, new_password if new_password else None)
                if resultado:
                    messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
                    actualizar_window.destroy()
                    self.ver_usuarios()  # Actualizar la tabla
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el usuario")
            except Exception as e:
                messagebox.showerror("Error", f"Error al actualizar usuario: {str(e)}")
        
        # Botones
        tk.Button(actualizar_window, text="Guardar Cambios", command=guardar_cambios).pack(pady=10)
        tk.Button(actualizar_window, text="Cancelar", command=actualizar_window.destroy).pack(pady=5)

    def eliminar_usuarios(self):
        # Verificar si hay un usuario seleccionado
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione un usuario para eliminar")
            return
        
        # Obtener datos del usuario seleccionado
        item = self.tree.item(seleccion[0])
        user_id, username = item['values']
        
        # Confirmar eliminación
        respuesta = messagebox.askyesno(
            "Confirmar Eliminación", 
            f"¿Está seguro de que desea eliminar al usuario '{username}' (ID: {user_id})?"
        )
        
        if respuesta:
            try:
                # Llamar a la función del controlador para eliminar usuario
                resultado = eliminar_usuario(user_id)
                if resultado:
                    messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
                    self.ver_usuarios()
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el usuario")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar usuario: {str(e)}")
    
    def cerrar_sesion(self):
        if messagebox.askyesno("Cerrar sesión", "¿Está seguro de que desea cerrar sesión?"):
            self.root.destroy()
                
