import random
# Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas), y
# los elementos de estas matrices deben ser aleatorios del 1 al 5, no se deben ingresar
# por consola. Luego se deben sumar en una función las matrices, y en otra función
# restarlas. En este caso no se puede utilizar numpy, solo estructuras propias de Python.

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
            elemento = random.randint(1,5)
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
print()

suma_matrices = sumar(m1,m2)

if suma_matrices == None:
    print('No se puede sumar matrices de distintas dimensiones.')
else:
    print('Suma:')
    mostrar_matriz(suma_matrices)

    resta_matrices = restar(m1,m2)
    if resta_matrices == None:
        print('No se puede restar matrices de distintas dimensiones.')
    else:
        print()
        print('Resta:')
        mostrar_matriz(resta_matrices)
        


