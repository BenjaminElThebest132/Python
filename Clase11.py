total_ingresos = 0

cantidad_pasajes = int(input("¿Cuántos pasajes deseas comprar?\n--> "))

for x in range(cantidad_pasajes):
    try:
     tipo_pasaje = input("Ingresa que pasaje quieres \n1.- Barato ($100) \n2.- Regular ($200) \n3.- Caro (300)\n--> ")
     precio = 0
     if tipo_pasaje == '1':
         precio = 100 
     elif tipo_pasaje == '2':
         precio = 200 
     elif tipo_pasaje == '3':
         precio = 300 
     else:
        print("Tipo de pasaje no válido. Por favor, elige entre Económico, Estándar o Premium.")
        continue
     
     total_ingresos += precio

    except ValueError:
        print("Necesitas proporcionar un valor numérico válido para el precio del pasaje.")
        break
print(f"El monto total obtenido por la venta de todos los pasajes es: ${total_ingresos}")