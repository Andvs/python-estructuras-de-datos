import numpy as np

matriz = np.array([[1.23456, 2.34567], [3.45678, 4.56789]])
inversa = np.linalg.inv(matriz)
np.set_printoptions(precision=2)
print(inversa)

# lista = [1, 2, 3, 4]
# lista.reverse()
# print(lista)  # Output: [4, 3, 2, 1]

# lista = [1, 2, 3, 4]
# lista_invertida = lista[::-1]
# print(lista_invertida)  # Output: [4, 3, 2, 1]
