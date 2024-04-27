print("Haz una contraseña\nque tenga estos requisitos: ")
print("1.-debe tener 8 caracteres (minimo)")
print("2.-Al menos una letra mayuscula y minuscula")
print("3.-Tiene que contener almenos 1 numero")

def verificar(contra):
     if len(contra) < 8:
       return "\tLa contraseña es demasiado corta."
     elif not any(c.upper() for c in contra):
      return "\tDebe contener al menos una letra mayúscula."
     elif not any(c.islower() for c in contra):
        return "\tDebe contener al menos una letra minúscula."
     elif not any(contra.isdigit() for contra in contra):
        return "\tDebe contener al menos un número."
     else:
        return "\tLa contraseña cumple con todos los requisitos."
contra = input("Ingresa una contraseña: ")
res = verificar(contra)
print(res)
""""
Defini verificar con condiciones y funciones como "upper" para las mayusculas "islower" para la minusculas "isdigit" para el numero y "len" para la capacidad de digitos tenga la contraseña (contra si es menor que < 8 esta malo)
Todo sacado de una gia de phyton ellibrodepython.com
El hecho de colocar un "c." Es para acortar la variable, solo funca si lo aplicas bien
"""
