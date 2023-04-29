import random

filas1 = int(input("Ingrese la cantidad de filas para la primera matriz: "))
columnas1 = int(input("Ingrese la cantidad de columnas para la primera matriz: "))

def matriz(filas1,columnas1):
    matriz=[]
    for i in range(filas1):
        fila=[]
        for j in range(columnas1):
            fila.append(random.randint(1,5))
        matriz.append(fila)
    return matriz
        
matriz1=matriz(filas1,columnas1)

filas2 = int(input("Ingrese la cantidad de filas para la segundsa matriz: "))
columnas2 = int(input("Ingrese la cantidad de columnas para la segunda matriz: "))

def matriz(filas2,columnas2):
    matriz=[]
    for i in range(filas2):
        fila=[]
        for j in range(columnas2):
            fila.append(random.randint(1,5))
        matriz.append(fila)
    return matriz
        
matriz2=matriz(filas2,columnas2)

def suma(matriz1, matriz2):
    filas=len(matriz1)
    columnas=len(matriz1[0])
    resultado=[]
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    return resultado
    
resultadosuma = suma(matriz1, matriz2)

def suma(matriz1, matriz2):
    filas=len(matriz1)
    columnas=len(matriz1[0])
    resultado=[]
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(fila)
    return resultado
    
resultadoresta = suma(matriz1, matriz2)

print (f"la primera matriz es:{matriz1}")
print (f"la segunda matriz es:{matriz2}")
print(f"la suma de ambas matrizes es:{resultadosuma}")
print(f"la suma de ambas matrizes es:{resultadoresta}")

