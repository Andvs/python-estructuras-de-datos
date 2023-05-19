#crear matriz con los datos que introduces:
#filas, columnas y valores para cada elemento

matriz = []
filas = int(input('Filas: '))
columnas = int(input('Columnas: '))

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        elemento = float(input(f'Elemento {i+1},{j+1}: '))
        matriz[i].append(elemento)

#mostrar matriz

for filas in matriz:
    print('[', end=' ')
    for i in filas:
        print(i, end=' ')
    print(']')
