# Se tiene una matriz A, donde la matriz inversa de A se representa como A−1
# la cual
# es una matriz cuadrada que hace que la multiplicacion´ A × A−1
# sea igual a la matriz
# identidad I. Realizar un algoritmo que compruebe la siguiente propiedad:
# A × A−1 = I, donde I es la Matriz Identidad

# creamos una matriz cuadrada (3x3) y la imprimimos en pantalla

A=[[10,10,0],[0,8,0],[5,0,4]]

# imprime las matrizes de forma mas ordenada,haciendo que se imprima cada fila hacia abajo.
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()

#imprimimos la matriz A

print("La matriz A es:")
imprimir_matriz(A)

#obtenemos la inversa de la matriz creada anteriormente

def inversa(A):

    #obtenemos el determinante de la matriz
    determinante = (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
    # si el determinante es 0 la matriz no es invertible por lo tanto el programa se cerrara
    if determinante == 0:
        print("La matriz A no es invertible.")
        
    #si el determinante es distinto de 0 ,continuamos buscando la matriz de cofactores
    else:
        cofactores = [[A[1][1] * A[2][2] - A[1][2] * A[2][1],-(A[1][0] * A[2][2] - A[1][2] * A[2][0]),A[1][0] * A[2][1] - A[1][1] * A[2][0]],
                   [-(A[0][1] * A[2][2] - A[0][2] * A[2][1]),A[0][0] * A[2][2] - A[0][2] * A[2][0],-(A[0][0] * A[2][1] - A[0][1] * A[2][0])],
                   [A[0][1] * A[1][2] - A[0][2] * A[1][1],-(A[0][0] * A[1][2] - A[0][2] * A[1][0]),A[0][0] * A[1][1] - A[0][1] * A[1][0]]]
    #luego buscamos la matriz adjunta              
        adjunta=[]
        for i in range(len(A)):
            filas=[]
            for j in range(len(A[0])):
                filas.append(cofactores[i][j])
            adjunta.append(filas)
    #finalmente obtenemos la inversa dibidiendo la matriz adjunta entre el determinante
        inversa = []
        for i in range(len(A)):
            fila=[]
            for j in range(len(A[0])):
                fila.append(adjunta[j][i]/determinante)
            inversa.append(fila)
        return inversa
    
# asignamos la matriz inversa a una variable y la imprimimos en pantalla 
     
A1=inversa(A)
print("La inversa A-1 es:")
imprimir_matriz(A1)

# realizamos la multiplicacion de la matriz A y su inversa

def multiplicar(A,A1):
    resultado=[]
    for i in range(len(A)):
        fila=[]
        for j in range(len(A1[0])):
            suma=0
            for k in range(len(A1)):
                suma = suma + A[i][k] * A1[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

# asignamos el resulatdo a una variable e imprimimos en pantalla

AxA1=multiplicar(A,A1)
print("El resultado de la multiplicacion (A × A−1) es:")
imprimir_matriz(AxA1)

# creamos la matriz identidad para realizar la compararcion

I=[[1,0,0],[0,1,0],[0,0,1]]
print("La matriz identidad es:")
imprimir_matriz(I)

# comparamos el resultado de la multiplicacion entre la matriz A y su inversa A-1 con la matriz identidad I,
# si el resultado de la multiplicacion es igual a la matriz identidad la propiedad se cumple 
# y si son distintos no se cumple
if AxA1 == I :
    print("Como A × A−1 = I la propiedad se cumple")
else:
    print("la propiedad no se cumple")