print ("Le vamos a mostrar su IMC (indice de masa corporal) Necesitaremos algunos datos")
pes = float(input("Su peso en KG: "))
alt = float(input("Su altura en metros: "))
imc = pes / (alt ** 2)
print (f"Tu IMC es: {imc:.2f}" )
""""
Ocupe el ":.2f" que indica que quiero formatear imc como un número de punto flotante con dos decimales después del punto.
"""



