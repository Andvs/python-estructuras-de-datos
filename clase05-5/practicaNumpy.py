# import numpy as np

# # Definir las matrices
# matriz1 = np.array([[1, 2, 3], [4, 5, 6]])  # Matriz de dimensiones 2x3
# matriz2 = np.array([[7, 8], [9, 10], [11, 12]])  # Matriz de dimensiones 3x2

# # Multiplicar las matrices
# resultado = np.dot(matriz1, matriz2)

# # Imprimir el resultado
# print(resultado)


import numpy as np

m1 = np.array([[1,2,3],[4,5,6]])
m2 = np.array([[7,8,7],[9,10,8]])

# resultado_pro= np.dot(m1,m2)
# resultado_rest = m1-m2
# resultado_sum = m1+m2
resultado_rest = np.subtract(m1,m2)
resultado_sum = np.add(m1,m2)
# print(resultado_pro)
print(resultado_rest)
print(resultado_sum)