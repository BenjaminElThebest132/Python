print("Ingrese los siguientes datos:")
nombre = input("Las 2 primeras letras de su primer nombre: ")
apellido = input("Las 2 primeras letras de su segundo apellido: ")
rut = input("Los 2 primeros números de su rut: ")
mes = input("Las 3 letras iniciales del mes de su nacimiento: ")
ciudad = input("Las 2 últimas letras de la ciudad donde vive: ")
opcion1 = nombre + apellido + rut + mes + ciudad
opcion2 = nombre + rut + apellido + mes + ciudad + mes
opcion3 = rut + nombre + mes + ciudad + apellido
opcion4 = apellido + rut + nombre + mes + ciudad + rut
opcion5 = ciudad + apellido + nombre +rut + mes + ciudad
print("")
print(f"La opción 1 de contraseña es: {opcion1}")
print(f"La opción 2 de contraseña es: {opcion2}")
print(f"La opción 3 de contraseña es: {opcion3}")
print(f"La opción 4 de contraseña es: {opcion4}")
print(f"La opción 5 de contraseña es: {opcion5}")

"""
No se cual es la correcta, yo digo que la 2 y la 4 no porque repiten variables. Pero ni idea :(
"""
