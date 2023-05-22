# Aplicar el metodo de Gauss para invertir una matriz aleatoria de 3 a 5 de dimensi ´ on sin ´
# utilizar librerias. Imprimir la matriz original y luego la matriz inversa. Recordar que si una
# matriz A es una matriz cuadrada no-singular, es decir, tal que su determinante es distinto
# de cero se puede utilizar el Metodo de Eliminaci ´ on Gaussiana
import random

filas=random.randint(3,5)
columnas=random.randint(3,5)

# se crea una matriz aleatoria de tamaño entre 3 a 5 con elemetos entre 1 y 9

def crear_matriz(filas, columnas):

    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = random.randint(1,9)
            fila.append(elemento)
        matriz.append(fila)
    return matriz

matriz=crear_matriz(filas,columnas)

# imprime la matriz de forma mas ordenada,haciendo que se imprima cada fila hacia abajo.
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()

print("la matriz es:")
imprimir_matriz(matriz)

# cambia las filas,verificando si el primer elemento es 1,si lo es devuelve la matriz original,
# sino verifica el primer elemento de cada fila de la matriz hasta encontrar alguna con el primer elemento 1
# y la intercambia por la primera fila

def cambiar_filas(matriz):

    if matriz[0][0] == 1:
        return matriz
    else:
        for i in range(len(matriz)):
            if matriz[i][0] == 1:
                matriz[0], matriz[i] = matriz[i], matriz[0]
        return matriz
    
matrizcambiada=cambiar_filas(matriz)
print("la matriz cambiada es:")
imprimir_matriz(matrizcambiada)

# si la funcion anterior devuelve la matriz original,este funcion hara que le primer elemento de la matriz sea 1,
# primero calcula el numero por el que dividira la primera fila para que le primer elemento de 1 ,dividiendo el 
# primer elemento de la matriz en 1,luego recorre toda la fila dividiendp cada numero por el divisor calculado.
# Y si la matriz ya tiene como primer elemeto un 1 devuelve la matriz original.

def dividir_filas(matriz):

    if matriz[0][0] != 1:
        divisor = matriz[0][0] / 1 
        for i in range(len(matriz[0])):
            matriz[0][i] = matriz[0][i] / divisor 
        return matriz
    else:
        return matriz

matrizdividida= dividir_filas(matriz)
print("la matriz dividida es:")
imprimir_matriz(matrizdividida)
    
