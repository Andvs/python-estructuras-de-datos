#3x2 2x4
def multi(m1, m2):
    if len(m1[0]) == len(m2):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(0)
                for k in range(len(m1[0])):
                    m3[i][j] += m1[i][k] * m2[k][j]
        return m3
    else:
        return None

    
a = [[1,2],
     [3,4],
     [5,6]]

b = [[1,2,3],
     [4,5,6]]

if multi(a,b) == None:
    print('No se puede multiplicar esas matrices.')
else:
    for filas in multi(a,b):
        print('[', end=' ')
        for elemento in filas:
            print(elemento, end=' ')
        print(']')




                    
                    

