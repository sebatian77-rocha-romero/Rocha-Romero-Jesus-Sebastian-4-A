productos = ["jugo", "cafe", "refresco"]
precios = [10, 15, 20]

def calcular_precio(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

# Menú de usuario
print("-----------TIENDA------------")
cantidades = []
print("Selecciona lo que vas a comprar: ")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad = int(input(f"¿Cuántos {productos[i]} quieres? "))
    cantidades.append(cantidad)

# Calcular total
total = calcular_precio(cantidades, precios)

# Imprimir ticket
print("\n\t\t----- TICKET DE COMPRA -----")
print("Producto\tCant.\tPrecio\tSubtotal")
print("-------------------------------------------")
for i in range(len(productos)):
    if cantidades[i] > 0:  # Solo mostrar si compró algo
        subtotal = cantidades[i] * precios[i]
        print(f"{productos[i]:<10}\t{cantidades[i]:<5}\t${precios[i]:<5}\t${subtotal}")

print("-------------------------------------------")
print(f"TOTAL:\t\t\t\t${total}")
print("-------------------------------------------")

