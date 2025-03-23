## LISTAS: POP()
#Quita a un elemento de una posicion dada

paises= ["Peru","Brasil","Argentina","Uruguay"]
print("Mi lista inicial:".format(paises))

paises.pop()

print("Mi lista actualizada es:".format(paises[2]))
paises.pop(2)
print("Mi lista actualizada es:{}".format(paises))

paises.pop(2)
print("Mi lista actualizada es:{}".format(paises[2]))
