import random
# Crear una matriz cuadrada de 5 × 5, y obtener la suma de todos los elementos de cada
# columna, e imprimir la suma mas alta entre las columnas. Adem ´ as obtener la suma de ´
# todos los elementos de las filas y la suma mas baja entre todas las filas. Sin utilizar la
# biblioteca numpy.


def crearMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            elemento = random.randint(1,9)
            matriz[i].append(elemento)
    return matriz

def mostrarMatriz(matriz):
    for filas in matriz:
        print('[', end=' ')
        for elemento in filas:
            print(elemento, end=' ')
        print(']')

#Crea una lista con la suma de los elementos de cada columna
def sumasColumnas(matriz):
    sumasColumnas = []
    
    for i in range(5):
        suma = 0
        for j in range(5):
            suma += matriz[j][i]
        sumasColumnas.append(suma)
    return sumasColumnas

#crea una lista con las suma de los elementos de cada fila
def sumasFilas(matriz):
    sumasFilas = []
    
    for i in range(5):
        suma = 0
        for j in range(5):
            suma += matriz[i][j]
        sumasFilas.append(suma)
    return sumasFilas


matriz = crearMatriz(5,5)
mostrarMatriz(matriz)

#se obtiene el mayor de las sumas de cada columna de la matriz
mayorSumaColumnas = max(sumasColumnas(matriz))
#se obtiene el menor de las sumas de cada fila de la matriz
menorSumaFilas = min(sumasFilas(matriz))


print(f'La suma más alta entre las columnas es: {mayorSumaColumnas}')
print(f'La suma más baja entre las filas es: {menorSumaFilas}')






