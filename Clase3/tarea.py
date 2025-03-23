"""
Requisitos:

- Crear dos lista de personas vacías
- Agregar los datos de nombre, edad y profesión para ambas listas
- Obtener y mostrar la suma de las edad // por índica
- Sumar ambas listas y mostrar el resultado en la terminal
- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando las edades de ambas personas
- Mostrar la lista vacía de la segunda persona aplicando el método respectivamente

"""

lista1=[]
lista2=[]
lista1.append("Dana")
lista1.append(19)
lista1.append("Ingeniera")
lista2.append("Dana")
lista2.append(19)
lista2.append("Ingeniera")

calc1= lista1[1] + lista2[1]
suma= lista1 + lista2

print(calc1)
print(suma)
print(suma.reverse())
lista1.remove(19)
lista2.remove(19)
lista2.clear()

""""
datos1= input("Ingrese datos: nombre,edad,profesion").split()
nombre,edad,profesion= datos1[0],datos1[1],datos1[2]

datos2= input("Ingrese datos: nombre,edad,profesion").split()
nombre,edad,profesion= datos2[0],datos2[1],datos2[2]
"""