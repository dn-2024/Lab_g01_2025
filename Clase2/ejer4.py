#bool

var1 = True
var2 = False
var3 = False
print("El valor de la variable var1 es: {}". format(var1))
print("El valor de la variable var2 es: {}". format(var2))

if var2:
    print("COMIENDO...")
if var3:
    print("DURMIENDO...")
    print(2025)
if var1:
    print("ESTUDIANDO...")

#se ejecutara solo el ultimo if porque es el unico que tiene un valor verdadero