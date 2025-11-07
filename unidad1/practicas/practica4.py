# PRACTICA 4: HERENCIA

class ticket:
    def __init__(self, id, tipo, prioridad):
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = "pendiente"

    def __str__(self):
            return f"[ID:{self.id}] Tipo:{self.tipo} | Prioridad:{self.prioridad} | Estado:{self.estado}"

class empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    def trabajar_en_ticket(self, ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")

class desarrollador(empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "software":
            ticket.estado = "resuelto"
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print("Este tipo de ticket no lo puede resolver el desarrollador")

class tester(empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "prueba":
            ticket.estado = "resuelto"
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print("Este tipo de ticket no lo puede resolver el tester")

class proyectmanager(empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"{self.nombre} asignó el ticket {ticket.id} al empleado {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)


# Crear tickets y empleados (instancias de objetos)
ticket1 = ticket(1, "software", "alta")
ticket2 = ticket(2, "prueba", "baja")

dev1 = desarrollador("Carlos")
tester1 = tester("Juan")
pm = proyectmanager("Mondongo")

pm.asignar_ticket(ticket2, dev1)  
pm.asignar_ticket(ticket1, tester1)

#asignar un menu interactivo con while y con if para:
#1.crear un ticket
#2.ver los tickets
#3.asignar un ticket
#4.salir del programa


tickets = []
contador_id = 1

desarrolador1 = desarrollador("Carlos")
tester1 = tester("Juan")
pm = proyectmanager("Mondongo")

import os

def limpiar_pantalla():
    os.system("cls")

def esperartecla():
    input("presiona enter para continuar...")

start=True
while start:
    print("\t\n 1.crear un ticket \t\n 2.ver los tickets\t\n 3.asignar un ticket \t\n 4.salir del programa")
    opcion=input("elija una opcion: ")

    if opcion == "1":
        tipo = input("Ingrese el tipo de ticket (software/prueba): ")
        prioridad = input("Ingrese la prioridad (alta/baja): ")
        nuevo = ticket(contador_id, tipo, prioridad)
        tickets.append(nuevo)
        print(f"Ticket {contador_id} creado.")
        contador_id += 1
        esperartecla()
        limpiar_pantalla()
        

    elif opcion == "2":
        if len(tickets) == 0:
            print("No hay tickets creados.")
        else:
            print("\n--- LISTA DE TICKETS ---")
            for i in tickets:
                print(i)
        esperartecla()
        limpiar_pantalla()

    elif opcion == "3":
        if len(tickets) == 0:
            print("No hay tickets para asignar.")
        else:
            for i in tickets:
                print(i)
            try:
                id_ticket = int(input("Ingrese el ID del ticket a asignar: "))
                ticket_encontrado = next((i for i in tickets if i.id == id_ticket), None)
                if ticket_encontrado:
                    print("1. Asignar a desarrollador (Carlos)")
                    print("2. Asignar a tester (Juan)")
                    empleado_opcion = input("Elija el empleado: ")
                    if empleado_opcion == "1":
                        pm.asignar_ticket(ticket_encontrado, desarrolador1)
                    elif empleado_opcion == "2":
                        pm.asignar_ticket(ticket_encontrado, tester1)
                    else:
                        print("Opción inválida.")
                else:
                    print("Ticket no encontrado.")
            except ValueError:
                print("Debe ingresar un número válido.")
        esperartecla()
        limpiar_pantalla()

    elif opcion == "4":
        print("Saliendo del programa...")
        start = False

    else:
        print("Opción inválida. Intente de nuevo.")