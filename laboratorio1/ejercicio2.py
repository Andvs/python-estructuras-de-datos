import random

m1_filas = int(input('Ingrese el número de filas de la matriz 1: '))
m1_columnas = int(input('Ingrese el número de columnas de la matriz 1: '))

escalar = int(input('Ingrese un escalar: '))
m1 = [[random.randint(0,5) for j in range(m1_columnas) for i in range(m1_filas)]]


