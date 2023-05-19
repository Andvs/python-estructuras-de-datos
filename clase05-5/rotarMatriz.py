#rotar una matriz 90 grados en el sentido de las manecillas de un relog.

matriz = [[11,12,13,14,15],
          [21,22,23,24,25],
          [31,32,33,34,35],
          [41,42,43,44,45]]

def rotar(matriz):
    rotada = []
    for i in range(len(matriz[0])):
        rotada.append([])
        for j in range(len(matriz)):
            rotada[i].append(matriz[len(matriz)-1-j][i])

    return rotada

r = rotar(matriz)

for filas in matriz:
    print('[', end=' ')
    for elemento in filas:
        print(elemento, end=' ')
    print(']')

print()
for filas in r:
    print('[', end=' ')
    for elemento in filas:
        print(elemento, end=' ')
    print(']')

