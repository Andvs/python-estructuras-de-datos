import random
# Aplicar el metodo de Gauss para invertir una matriz aleatoria de 3 a 5 de dimensi ´ on sin ´
# utilizar librerias. Imprimir la matriz original y luego la matriz inversa. Recordar que si una
# matriz A es una matriz cuadrada no-singular, es decir, tal que su determinante es distinto
# de cero se puede utilizar el Metodo de Eliminaci ´ on Gaussiana.

def crearMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            elemento = random.randint(1,9)
            matriz[i].append(elemento)
    return matriz

def crearMatrizIdentidad(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            if i == j:
                matriz[i].append(1)
            else:
                matriz[i].append(0)
    return matriz

def mostrarMatriz(matriz):
    for filas in matriz:
        print('[', end=' ')
        for elemento in filas:
            print(elemento, end=' ')
        print(']')

def calcularInversa(matriz):
    filaActual = matriz[0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i != j  and matriz[i][j] != 0:
                filaActual = multiplicarListas(filaActual, matriz[i+1][j+1])
    return matriz

def multiplicarListas(lista, num):
    num = 2
    resultado = []
    for elemento in lista:
        resultado.append(elemento*num)
    return resultado

def restarListas(lista1,lista2):
    resultado = []
    for i in range(len(lista1)):
        resultado.append(lista1[i]-lista2[i])
    return resultado


# [ 1 0 0 ]
# [ 0 1 0 ]
# [ 0 0 1 ]



dimension = random.randint(3,5)
matriz = crearMatriz(dimension,dimension)
identidad = crearMatrizIdentidad(dimension,dimension)

mostrarMatriz(identidad)



