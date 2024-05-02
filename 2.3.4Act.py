edad = int(input("Para continuar debe darme su edad: "))
if edad >= 18:
    print("Es usted mayor de edad, continue.")
"""
"""
userUno = "Benja"
PassUno = "Rodrigo"
UserDos = "Aburto"
PassDos = "Collio"
user = input("Ingrese su usuario: ")
contra = input("Ingrese su contraseña: ")

if (user == "Benja" and contra == "Rodrigo") or (user == "Aburto" and contra == "Collio"):
    print ("Bienvenido")
else:
    print("Usuario o/y contraseña incorrectos")
"""
"""
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 4.0:
    print(f"Aprobado, su promedio es de: {promedio:.2f} ")
else:
    print(f"Reprobado, su promedio es de: {promedio:.2f}")
"""
"""
respuesta = input("¿Cuál de los siguientes animales vive en el agua? \nA-Perro \nB-Cocodrilo \nC-Conejo \nD-Tiburón \n: ")
puntaje = 0
if respuesta.lower() == "b":
    puntaje += 0.5
elif respuesta.lower() == "d":
    puntaje += 1.0
print(f"El puntaje obtenido es: {puntaje}")
"""
"""







