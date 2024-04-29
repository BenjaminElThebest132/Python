edad = int(input("Para continuar debe darme su edad: "))
if edad >= 18:
    print("Es usted mayor de edad, continue.")

"""
No entendi esta actividad
"""
"""
"""
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 4.0:
    print(f"Aprobado, su promedio es de: {promedio} ")
else:
    print(f"Reprobado, su promedio es de: {promedio}")
"""
"""
respuesta = input("¿Cuál de los siguientes animales vive en el agua? \n-Perro \n-Cocodrilo \n-Conejo \n-Tiburón \n: ")
puntaje = 0
if respuesta == "cocodrilo":
    puntaje += 0.5
elif respuesta == "tiburón":
    puntaje += 1.0
print(f"El puntaje obtenido es: {puntaje}")



