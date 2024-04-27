print("Ingresar los datos de la venta")
cliente = input("Ingrese el nombre del cliente: ")
precio1 = int(input("Ingrese el precio del producto1: "))
cantidad1 = int(input('La cantidad de "producto1": '))
precio2 = int(input("Ingrese el precio del producto2: "))
cantidad2 = int(input('La cantidad del "producto2": '))
precio3 = int(input("Ingrese el precio del producto3: "))
cantidad3 = int(input('La cantidad del "producto3": '))
total_bruto = (precio1*cantidad1) + (precio2*cantidad2) + (precio3*cantidad3)
iva = round(total_bruto * 0.19)
print("")
print(f"Cliente: \t{cliente}")
print(f"Total bruto:\t${total_bruto}")
print(f"Iva: \t\t${iva}")
print("Total a pagar: ", iva+total_bruto)
"""
Simplemente habia que ordenar, y arreglar las variables para la suma de los productos los cuales se ubican (le quite el tema del descuento pero es simplemente aplicar otra variable que sea tipo INT "descuento = int(input("Ingrese su descuento: ")) Y despues hacer un algoritmo matematico para aplicarlo que seria des = (totalbruto*descuento)/100 y ponerlo con un "\t"
"""