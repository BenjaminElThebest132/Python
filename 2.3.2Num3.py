user = input("Ingrese el usuario: ")
pwd = input("Ingrese su password: ")
if user == "duoc" and pwd == "123duoc":
 valorDev = int(input("Bienvenido, Ingrese el valor a devolver: "))
 if valorDev > 100000:
    print("Se dará la máxima urgencia a su devolución de dinero")
 else:
   print("El caso ha quedado registrado, le informaremos lo antes posible") 
else:
   print("Error en contraseña")
""""
Respondiendo a la pregunt del problema, si ponemos mal la contraseña el IF pasa al ELSE de "Error en la contraseña" Y si pasamos con el usuraio correcto e ingresamos la el monto de 120k Se nos dira "Se dará la máxima urgencia a su devolución de dinero"
"""
