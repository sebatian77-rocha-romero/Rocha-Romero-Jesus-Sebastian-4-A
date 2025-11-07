#practica 5 singleton


class logger:
    #atributo de la clase para ayudar la unica instancia
    _instancia = None

 #metodo __new__ controloa la creacion del objeto antes de init, se asegura que solo exista una unica instancia en el logger
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.archivo = open("app.log", "a")
        return cls._instancia
    
    def registro(self, mensaje):
        self.archivo.write(mensaje + "\n")
        self.archivo.flush() #forzar al archvio para guardarse en el disco

registro1 = logger() #creamos la unica instancia singletosn
registro2 = logger() #devuelkve la misma instancia, sin crear una nueva

registro1.registro("inicio de sesion en la aplicacion")
registro2.registro(" el usuario se autentica")

print(registro1 is registro2)

