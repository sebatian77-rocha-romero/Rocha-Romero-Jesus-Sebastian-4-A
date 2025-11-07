#practica 2 claes, objetos, metodos y atributos

class persona:
    def __init__(self, nombre, apellido, edad,):
        #creacion de atributos
        self.nombre= nombre
        self.apellido=apellido
        self.edad =edad
        self.__cuenta = None #atributo privado

    def asignar_cuenta(self, cuenta):
        self.__cuenta = cuenta
        print(f"{self.nombre} ahora tiene una cuenta bacaria")

    
    def consultar_saldo(self):
        if self.__cuenta:
            print(f"Eel saldo de {self.nombre} es: $ {self.__cuenta}") #saldo
        else:
            print(f"{self.nombre} no tiene una cuenta bancaria")

    def consultar_saldo(self):
        if self.__cuenta:
            print(f"El saldo de {self.nombre} es: $ {self.__cuenta.mostrar__saldo()}")
        else:
            print(f"{self.nombre} no tiene una cuenta bancaria")

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, mi apellido es {self.apellido}, y tengo {self.edad} años")

    def cumplir_años(self):
        self.edad += 1
        print(f"Esta persona cumplió: {self.edad} años")


class cuenta_bancaria:
    def __init__(self, num_cuenta, saldo):
        self.num_cuenta = num_cuenta
        self.__saldo = saldo  # atributo privado

    def mostrar__saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se depositó la cantidad de $ {cantidad} a la cuenta")
        else:
            print("Ingrese una cantidad válida")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se retiró la cantidad de $ {cantidad}")
        else:
            print("Fondos insuficientes o cantidad inválida")


# Creación del objeto o instancia de una clase:
persona1 = persona("Miguel", "Juan", 20)
cuenta1 = cuenta_bancaria("001", 500)

# Asignar cuenta a la persona
persona1.asignar_cuenta(cuenta1)

# Probar métodos
persona1.consultar_saldo()
cuenta1.depositar(200)
cuenta1.retirar(100)
persona1.consultar_saldo()
######


#ejercisio 1
#crear una clase, objeto, min 3 atributos, min 3 metodos
class tienda:
    def __init__(self, producto, tipo, precio):
         #creacion de atributos
        self.producto=producto
        self.tipo=tipo
        self.precio=precio

    def info(self):
        print(f"compro {self.producto}, de la categoria {self.tipo}, y cuesta ${self.precio},")

    #IVA
    def calcular_iva(self):
        iva = self.precio * 0.16
        total = self.precio + iva
        print(f"Precio base: ${self.precio}")
        print(f"IVA (16%): ${iva}")
        print(f"Total a pagar: ${total}")
        return total
    
    #Actualizar precio
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        print(f"Precio actualizado: ${self.precio}")


compra1 = tienda("Lavadora", "Electrodoméstico", 1500)
compra2 = tienda("Televisor", "Electrónica", 800)
compra3 = tienda("Refrigerador", "Electrodoméstico", 2000)

print("=== COMPRA 1 ===")
compra1.info()
compra1.calcular_iva()

print("\n=== COMPRA 2 ===")
compra2.info()
compra2.actualizar_precio(750)

print("\n=== COMPRA 3 ===")
compra3.info()
compra3.calcular_iva()
compra3.actualizar_precio(750)
    