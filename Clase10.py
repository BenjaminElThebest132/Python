try:
    totalpagar_liviano = 0
    totalpagar_normal = 0
    Sacos_livianos = 0
    Sacos_normales = 0
    cantidad_sacos = int(input("Ingrese la cantidad de sacos: "))

    for x in range(cantidad_sacos):
        peso = int(input(f"Ingrese el peso del saco en KG {x+1}: "))
        if peso >= 1 and peso <= 5:
            totalpagar_liviano += 1000
            Sacos_livianos += 1
        elif peso >= 6 and peso <= 10:
            totalpagar_normal += 2000
            Sacos_normales += 1
        else:
            print("El peso ingresado no es válido. Debe estar entre 1 y 10 kilos.")

    print(f"{Sacos_livianos} sacos livianos de $1,000")
    print(f"{Sacos_normales} sacos normales de $2,000")
    print(f"Valor total a pagar: ${totalpagar_liviano+totalpagar_normal}")

except ValueError:
    print("Error: Por favor ingrese un número válido.")