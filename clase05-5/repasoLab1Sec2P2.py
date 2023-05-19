import random
# Crear una matriz la cual se debe solicitar por teclado la cantidad de filas y columnas que va a
# contener. También ingresar por consola un escalar. Los elementos de la matriz deben ser
# generados aleatoriamente (0 al 10). Por último, se debe multiplicar la matriz generada por el
# escalar ingresado.

def crearMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            elemento = random.randint(0,10)
            matriz[i].append(elemento)
    return matriz

def mostrar_matriz(m):
    for filas in m:
        print('[', end=' ')
        for elemento in filas:
            print(elemento, end=' ')
        print(']')

def multiplicar_escalar(matriz, escalar):
    resultado = []
    for i in range(len(matriz)):
        resultado.append([])
        for j in range(len(matriz[0])):
            resultado[i].append(matriz[i][j]*escalar)
    return resultado

print('Matriz')

filas = int(input('Filas: '))
columnas = int(input('Columnas:'))
m = crearMatriz(filas, columnas)
print()
mostrar_matriz(m)
print()

escalar = int(input('Ingrese un escalar para multiplicarlo por la matriz:'))

print('Matriz resultado: ')
print()
matriz_multi = multiplicar_escalar(m, escalar)
mostrar_matriz(matriz_multi)




