#Transponer los elementos de las filas
#a las columnas y los elementos de las columnas a las filas.

# m = [[1,2,3],
#      [4,5,6]]

# t = [[1,4],
#      [2,5],
#      [3,6]]

m = [[1,4],
      [2,5],
      [3,6]]

def transpuesta(matriz):
    transpuesta = []
    for i in range(len(matriz[0])):
        transpuesta.append([])
        for j in range(len(matriz)):
            transpuesta[i].append(m[j][i])
    return transpuesta

t = transpuesta(m)
print(t)
for filas in t:
    print('[', end= ' ')
    for elemento in filas:
        print(elemento, end=' ')
    print(']')

    #con numpy:
    #matriz = np.array([[1, 2, 3], [4, 5, 6]])
    #transpuesta_funcion = np.transpose(matriz)