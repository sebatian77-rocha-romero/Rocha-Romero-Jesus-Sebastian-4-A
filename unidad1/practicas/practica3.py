#practica 3: introduccion al poliformismo
#simular un sistema de cobro de almenos 4 tipos de opciones de pago 

class pago_tarjeta:
    def procesar_pago(self, cantidad):
        return f"procesando pago de $ {cantidad} con tarjeta de debito/credito"

class paypal:
    def procesar_pago(self, cantidad):
        nombre=input("ingrese su nombre: ")
        return f"procesando pago de $ {cantidad} con paypal, a nombre de {nombre}"

class efectivo:
    def procesar_pago(self, cantidad):
        return f"procesando pago de $ {cantidad} en efectivo"

class oxxo:
    def procesar_pago(self, cantidad):
        cantidad_total = cantidad + 20
        return f"procesando pago de $ {cantidad} realizada en oxxo,  ${cantidad_total} con tarifa del 20% "

metodos_pago=[pago_tarjeta(), paypal(), efectivo(), oxxo()]

for m in metodos_pago:
    print(m.procesar_pago(500))

#ACTIVIDAD1
#procesar diferentes cantidades en cada opcion de pago: 100 con tarjeta, 400 con paypal, 600 con deposito, 500 con cheque

pago1 = pago_tarjeta()
pago2 = paypal()
pago3 = oxxo()
pago4 = efectivo()

print(pago1.procesar_pago(100))
print(pago2.procesar_pago(400))
print(pago3.procesar_pago(600))
print(pago4.procesar_pago(500))

#ACTIVIDAD2: Agregar funcionalidad adicional a metodo procesar_pago() cuando sea deposito: sumar 20 (comision) a cantidad.
#cuando sea paypal, pedirle al usuario su nombre.



