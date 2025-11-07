import tkinter as tk
from tkinter import messagebox
from auth_controller import validar_credenciales
from deshboard_view import DashboardApp
from user_view import UserApp
from user_controller import *
from products_view import UserApp2


class LoginApp:
    def __init__(self, root):
        self.root = root;
        self.root.title("inicio de sesion")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        #Encabezado
        tk.Label(root, text="bienvenido al sistema", font= ("Comic Sans SM", 16, "bold")).pack(pady=16)

        #campos
        tk.Label(root, text="ingresa el nombre de usuario").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        #campos textp
        tk.Label(root, text="ingresa tu contraseña").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        #button
        tk.Button(self.root, text="Iniciar sesión", command=self.login).pack(pady=20)

    def login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showinfo("Faltan datos. Favor de ingresar usuario y contraseña")
            return

        if validar_credenciales(usuario, password):
            messagebox.showinfo("Acceso permitido", f"Bienvenido {usuario}")
            self.root.destroy()
            App = UserApp2(usuario)
        else:
            messagebox.showerror("Acceso denegado", "Tus datos son incorrectos, no se pudo ingresar.")

def iniciar():    
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()