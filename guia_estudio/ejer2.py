# 2. Se tiene una tupla con las siguientes frutas:
# frutas = (“manzana”, “platano”, “pera”, “naranja”, “frutilla”, “manzana”) ´
# Realizar las siguientes operaciones:
# a) Eliminar los elementos repetidos de la tupla.
# b) Agregar la fruta “mango” por teclado.
# c) Eliminar la fruta platano. ´
# d) Calcular la cantidad de frutas que existen.

frutas = ("manzana", "platano", "pera", "naranja", "frutilla", "manzana") 

print(f'Lista original: {frutas}')
#a)

lista_frutas = []

for i in frutas:
    if not(i in lista_frutas):
        lista_frutas.append(i)

frutas = tuple(lista_frutas)

#Convertirlo a set, así se eliminan los repetidos
# frutas = tuple(set(frutas))

print(f'a. Eliminar los elementos repetidos: {frutas}')


#b)

nueva_fruta = (input('Nueva fruta: '),)
frutas += nueva_fruta
print(f'b. Agregar "mango" por teclado: {frutas}')


#c)

lista_frutas = list(frutas)
lista_frutas.remove('platano')

frutas = tuple(lista_frutas)
print(f'c. Eliminar fruta platano: {frutas}')
#d)

num_frutas = len(frutas)
print(f'd. Calcular la cantidad de frutas que existen: {num_frutas}')



