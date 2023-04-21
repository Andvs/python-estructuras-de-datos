import array
import random
# Crear un arreglo aleatorio de tamaño entre 10 a 30. Imprimir el arreglo
# creado y luego solicitar por consola la búsqueda de un elemento en
# específico del arreglo creado. Todo esto utilizando import array.
lista = list(range(1,26))
random.shuffle(lista)
array1 = array.array('I', lista)
print(array1)

n = int(input('¿Que elemento quieres buscar? '))
print(f'El elemento {n} esta en la posición {array1.index(n)+1}.')


