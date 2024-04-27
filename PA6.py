import random

#No se pq se importa un random, tengo que preguntarle profe

numero1 = random.randint(1, 100)
numero2 = random.randint(1, 100)

#Se tiene que colocar a la funcion rand (random) INT para que sea un numero, vola lol

adivinar = int(input(f"¿Cuál es la suma de {numero1} y {numero2}? "))

suma = numero1 + numero2

if adivinar == suma:
    print("¡Correcto! La suma es igual a", suma)
else:
    print(f"Incorrecto. La suma correcta era {suma}.")