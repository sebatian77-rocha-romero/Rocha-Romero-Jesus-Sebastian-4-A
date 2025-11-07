import tkinter as tk
from tkinter import messagebox, ttk

from user_controller import ver_usuarios, agregar_usuarios, actualizar_usuarios, eliminar_usuario

#from user_controller import ver_usuarios, crear_conexion, actualizar_usuarios, eliminar_usuarios

class DashboardApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"bienvenido {username}")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        self.crear_elementos()
        self.ver_usuarios()
        self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root, text=f"hola {self.username}",
        font=("Comic Sans MS", 22, "bold")).pack(pady=10)

        tk.Button(self.root, text="ver usuarios", width=20, command=self.ver_usuarios).pack(pady=10)
        tk.Button(self.root, text="agregar usuarios", width=20, command=self.agregar_usuarios).pack(pady=10)
        tk.Button(self.root, text="actualizar usuarios", width=20, command=self.actualizar_usuarios).pack(pady=10)
        tk.Button(self.root, text="eliminar usuarios", width=20, command=self.eliminar_usuarios).pack(pady=10)
        tk.Button(self.root, text="cerrar sesion", width=20, command=self.cerrar_sesion).pack(pady=20)

        # Crear tabla de ver usuarios
        self.tree = ttk.Treeview(self.root, columns=("ID", "username"), show="headings", height=30)
        self.tree.heading("ID", text="ID usuario")
        self.tree.heading("username", text="nombre de usuario")
        
        # Configurar el ancho de las columnas
        self.tree.column("ID", width=200)
        self.tree.column("username", width=200)
        
        self.tree.pack(padx=20, pady=19, fill="both", expand=True)

    
   
   
   
'''''
def agregar_usuarios(self):
    messagebox.showinfo("agregar usuarios", "funcion para agregar usuario")

def actualizar_usuarios(self):
    messagebox.showinfo("actualizar usuarios", "funcion para actualizar usuario")

def eliminar_usuarios(self):
    messagebox.showinfo("eliminar usuarios", "funcion para eliminar usuario")

def cerrar_sesion(self):
    self.root.destroy()
'''''
