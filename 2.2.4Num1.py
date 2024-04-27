nom = input ("Ingrese nombre: ")
rut = input ("Ingrese rut: ")
ht = int(input ("Ingrese las horas trabajadas: "))
vh = int(input("Ingrese el valor hora del empleado: "))
colacion = int(5500)
movi = int(3000)
resu = (vh * ht)+colacion+movi
print(f"\tLiquidacion")
print(f"NOMBRE EMPLEADO: {nom}")
print(f"RUT EMPLEADO: {rut}")
print(f"MOVILIZACIÓN: {movi}")
print(f"ALIMENTACIÓN: {colacion}")
print(f"PAGO A EMPLEADO: {resu}")

"""
Habia que ordernar las variables relacionados con los prints para, para que no hubiera conflicto en el codigo
"""