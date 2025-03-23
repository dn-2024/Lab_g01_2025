## RECONOCIMIENTO DE TIPOS DE DATOS: TYPE()

#Creando variables
nombre= "Juan"
ciudad= "Buenos Aires"
saldo= 1000.50
empresa= "IBM"
correo= "juan@gmail.com"
empleado = [nombre, saldo, empresa, ciudad, correo]
empleado_dict = {"nomb": "Juan", "sald": 1000.50, "empre": "IBM", "ciud": "Buenos Aires", "correo": "juan@gmail.com"}

print("Tipo de dato de la variable nombre es {} ". format(type(nombre)))
print("Tipo de dato de la variable ciudad es {} ". format(type(ciudad)))
print("Tipo de dato de la variable saldo es {} ". format(type(saldo)))
print("Tipo de dato de la variable empresa es {} ". format(type(empresa)))
print("Tipo de dato de la variable correo es {} ". format(type(correo)))
print("Tipo de dato de la variable empleado es {} ". format(type(empleado)))
print("Tipo de dato de la variable empleado_dict es {} ". format(type(empleado_dict)))