producto = input ("Ingrese el nombre del producto: ")
valorProducto = int(input("Ingrese el valor del producto: "))
valorNeto = float(0.81)
valorSinIva = float(valorProducto * valorNeto)
print(f"-----Detalle producto----")
print(f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valorProducto}")
print(f"VALOR PRODUCTO SIN IVA: {valorSinIva}")
"""
La variable "Valor neto" y la variable "ValorSinIVA" Tienen que estar en funcion float para que puedan recibir datos en con coma (,) Se podria aplicar la funcion "redond" Para redondiar la variable, pero no es necesaria en tema de de dinero.
"""