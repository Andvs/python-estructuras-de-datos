import random

#Crear un arreglo y ordenarlo de forma descendente

lista = [5,4,3,2,1]
for i in range(len(lista)):
        if i != len(lista)-1:
            if (lista[i] > lista[i+1]):
                a = lista[i]
                lista.remove(lista[i])
                lista.insert(i+1,a)

print(lista)


# Luego ordenar ese mismo arreglo de forma aleatoria
random.shuffle(lista)
print(lista)

    