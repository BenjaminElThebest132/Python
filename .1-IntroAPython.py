#numeros compelejos
numeroComplejo= 1j
print(type(numeroComplejo))
#Datos de tipo rango range
coordenada = range(9)
print (coordenada)
print(type(coordenada))

# Datos set() Conjunto
numneros = {2,3,5,7,9}
numneros.add(13)
print(numneros)
letras = set("Pyrthon3")
letras.remove("3")
print(letras)
print(type(letras))
"""
Frozenset: Es una collecion inmutable parecida a un set. es inmutable
"""
frutas = frozenset({"manzana","betarraga","platano"})
print(frutas)
"""
Bytes: Es un tipo de dato inmutable, representa una secuencia de datos hasta el 0-255 
"""
#Crear un objeto a partir de un bytes
variableBytes=bytes("hola que es lo que realmente pasa", "utf-8")
print(variableBytes)

#Crear un texto a partid de numeros bytes
b = bytes([72, 111, 108, 97])
print(b)

#byteArray
c= bytearray("hola que pasa realmente","utf-8")
print(c)

#MODIFICAR
c[0] = 83
print(c)

#Datps de tipo none: Es un tipo de dato unico que no representa un valor.
variableNone= None
print(variableNone)

hola = "Hola bebe"
print(hola[5:9])
print("hola 'Duoc' ")