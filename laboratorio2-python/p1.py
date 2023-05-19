import random
import numpy as np

def crearMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            elemento = float(input(f'Ingresa el elemento {i+1},{j+1}:'))
            matriz[i].append(elemento)
    return matriz

def restarMatrices(m1,m2):
    resta = []
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in range(len(m1)):
            resta.append([])
            for j in range(len(m1[0])):
                resta[i].append(m1[i][j] - m2[i][j])
        return resta
    else:
        return None

def mostrarMatriz(matriz):
    for filas in matriz:
        print('[', end=' ')
        for elemento in filas:
            print(elemento, end=' ')
        print(']')

filas_random = random.randint(2,5)
print(f'Numero de filas: {filas_random}')
columnas_random = random.randint(2,5)
print(f'Numero de clumnas: {columnas_random}')
print()

print('Matriz 1')
matriz_1 = crearMatriz(filas_random, columnas_random)
print('Matriz 1')
mostrarMatriz(matriz_1)

print()
print('Matriz 2')
matriz_2 = crearMatriz(filas_random, columnas_random)
print('Matriz 2')
mostrarMatriz(matriz_2)
print()

print('Matriz resta')
resta_matrices = restarMatrices(matriz_1, matriz_2)
mostrarMatriz(resta_matrices)
print()

#matriz 3

print('Matriz 3')
filas_matriz_3 = int(input('Cantidad de filas: '))
columnas_matriz_3 = int(input('Cantidad de columnas: '))
matriz_3 = crearMatriz(filas_matriz_3, columnas_matriz_3)

#Multiplicar matiz con numpy

multiplicacion_matrices = np.dot(resta_matrices, matriz_3)
#2x3 3x5
if len(resta_matrices[0]) == len(matriz_3):
    print('Matriz multiplicación')
    mostrarMatriz(multiplicacion_matrices)
else:
    print()
    print('No se puede realizar la multiplicación de matrices.')
    print('Las cantidad de columnas de la primera matriz debe ')
    print('ser igual a la cantidad de filas de la segunda matriz.')
# 5x3 3x3 3x3

#comprobar la propiedad de las matrices transpuestas
#(A*B)t = Bt * At
matriz_A = resta_matrices
matriz_B = matriz_3

matriz_At = np.transpose(matriz_A)
matriz_Bt = np.transpose(matriz_B)

matriz_AB = np.dot(matriz_A, matriz_B)
matriz_ABt = np.transpose(matriz_AB)

matriz_BtxAt = np.dot(matriz_Bt, matriz_At)

print()
print('Ahora probaremos la propiedad de las matrices compuestas')
print('(A*B)t = Bt * At')

print()
print('Matriz (A*B)t')
print(matriz_ABt)
print()
print('Matriz Bt * At')
print(matriz_BtxAt)
print()
print('Se cumple la propiedad. Las matrices son iguales.')
#2x4 4x2
