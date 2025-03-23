#crear variables para los valores de nombre, profesion y ciudad
#Crear 2 variables para la remuneracion de enero y febrero
#Crear 1 variable para donde se sumará el ingreso de los meses de enero y febrero
#Mostrar en pantalla el mensaje de: "hola soy "nombre" y mi remuneracion acumulada es de " "

#creando variables
nombre= "Juan"
profesion= "Ingeniero"
ciudad= "Buenos Aires"

rem_ene= 1000
rem_feb= 2000
rem_acum= rem_ene + rem_feb

#imprimir los valores de las variables
print("Hola soy {} y mi remuneracion acumulada es de {} soles". format(nombre, rem_acum))
