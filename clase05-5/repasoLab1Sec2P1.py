import random

# Crear un algoritmo donde se solicite dos matrices por consola. Tanto la cantidad de columnas
# como de filas, deben ser ingresadas por teclado. Los elementos de las matrices deben ser
# generados de forma aleatoria (0 al 5). Estas dos matrices se deben sumar. Luego se solicita
# una tercera matriz. Al igual que las dos anteriores, se ingresan columnas y filas por consola, y
# sus elementos son generados aleatoriamente (0 a 5). Esta última matriz se restará con la
# matriz resultante entre la operación de suma.

def sumar(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] + m2[i][j])
        return m3
    else:
        return None

def restar(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] - m2[i][j])
        return m3
    else:
        return None

def crearMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            elemento = random.randint(0,5)
            matriz[i].append(elemento)
    return matriz

def mostrar_matriz(m):
    for filas in m:
        print('[', end=' ')
        for elemento in filas:
            print(elemento, end=' ')
        print(']')


print('Matriz 1')
filas_m1 = int(input('Filas: '))
columnas_m1 = int(input('Columnas:'))
m1 = crearMatriz(filas_m1, columnas_m1)
mostrar_matriz(m1)

print()
print('Matriz 2')
filas_m2 = int(input('Filas: '))
columnas_m2 = int(input('Columnas:'))
m2 = crearMatriz(filas_m2, columnas_m2)
mostrar_matriz(m2)

suma_matrices = sumar(m1,m2)

if suma_matrices == None:
    print('No se puede sumar dos matrices de distintas dimensiones')
else:
    print()
    print('Suma')
    mostrar_matriz(suma_matrices)
    print()
    print('Matriz 3')
    filas_m3 = int(input('Filas: '))
    columnas_m3 = int(input('Columnas:'))
    m3 = crearMatriz(filas_m3, columnas_m3)
    mostrar_matriz(m3)

    resta_matrices = restar(suma_matrices, m3)
    if resta_matrices == None:
        print('No se puede restar dos matrices de distintas dimensiones')
    else:
        print()
        mostrar_matriz(resta_matrices)



    




    







    


