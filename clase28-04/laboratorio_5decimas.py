import numpy as np

# Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas), y
# se debe añadir uno por uno los elementos de ambas matrices. Luego se deben sumar
# estas matrices en una función, y en otra función restarlas. Solo utilizando las funciones
# de la biblioteca numpy.


#Matriz 1
filas_m1 = int(input('Ingrese la cantidad de filas para la matriz 1: '))
columnas_m1 = int(input('Ingrese la cantidad de columnas para la matriz 1: '))

m1 = np.zeros((filas_m1, columnas_m1))

for i in range(filas_m1):
    for j in range(columnas_m1):
        valor = int(input(f"Ingrese el valor del elemento ({i+1}, {j+1}) de la matriz 1: "))
        m1[i][j] = valor

#Matriz 2
filas_m2 = int(input("Ingrese la cantidad de filas para la matriz 2: "))
columnas_m2 = int(input("Ingrese la cantidad de columnas para la matriz 2: "))

m2 = np.zeros((filas_m2, columnas_m2))

for i in range(filas_m2):
    for j in range(columnas_m2):
        valor = int(input(f"Ingrese el valor del elemento ({i+1}, {j+1}) de la matriz 2: "))
        m2[i][j] = valor


#suma

suma_matriz = np.add(m1, m2)

# Resta
resta_matriz = np.subtract(m1, m2)

print("Matriz 1:")
print(m1)

print("Matriz 2:")
print(m2)

print("Resultado de la suma:")
print(suma_matriz)

print("Resultado de la resta:")
print(resta_matriz)


