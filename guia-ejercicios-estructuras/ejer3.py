# Obtener la determinante de una matriz de 3 x 3 con sus elementos aleatorios.
import random

# definimos el tamaño de la matriz

filas=3
columnas=3

# creamos la matriz y agregamos elementos aleatorios entre 0,10

def matriz(filas,columnas):
    matriz=[]
    for i in range(filas):
        filas=[]
        for j in range(columnas):
            filas.append(random.randint(0,10))
        matriz.append(filas)
    return matriz

A=matriz(filas,columnas)

# imprime la matriz de forma mas ordenada,haciendo que se imprima cada fila hacia abajo.

def imprimir_matriz(matriz):
    for fila in matriz: 
        print(fila)
    print()

print("la matriz A es:")
imprimir_matriz(A)

# obtenemos el determinante

def det(A):

    proceso = (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
    return proceso

# asignamos el resulatdo a una varieble y la imprimos en pantalla

determinante = det(A)
print(f"el determinante de la matriz A es: {determinante}")