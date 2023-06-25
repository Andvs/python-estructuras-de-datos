# Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas), y
# se debe añadir uno por uno los elementos de ambas matrices. Luego se deben sumar
# estas matrices en una función, y en otra función restarlas. Solo utilizando las funciones
# de la biblioteca numpy.

import numpy as np

def crea_matriz(filas, columnas):
    matriz = np.zeros((filas,columnas))

    for i in range(filas):
        for j in range(columnas):
            elemento = float(input(f'Ingrese el elemento {i+1},{j+1}: '))
            matriz[i][j] = elemento
    return matriz

def sumar_matrices(matriz1, matriz2):
    resultado = matriz1 + matriz2
    return resultado

def restar_matrices(matriz1, matriz2):
    resultado = matriz1 - matriz2
    return resultado

filas = int(input('Filas: '))
columnas = int(input('Columnas: '))
print('Ingrese los elementos de la matriz 1: ')
matriz1 = crea_matriz(filas, columnas)
print('Ingrese los elementos de la matriz 2: ')
matriz2 = crea_matriz(filas, columnas)

resultado_suma = sumar_matrices(matriz1, matriz2)
print('Resultado de la suma de las matrices:')
print()
print(resultado_suma)

resultado_resta = restar_matrices(matriz1, matriz2)
print('Resultado de la resta de las matrices:')
print()
print(resultado_resta)




    