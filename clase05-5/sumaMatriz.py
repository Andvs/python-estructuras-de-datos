def suma(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] + m2[i][j])
        return m3
    else:
        return None

a = [[21,18,35,40],
     [19,11,21,14],
     [12,15,20,30]]

b = [[11,7,21,32],
     [9,15,24,10],
     [23,8,12,22]]
        
if suma(a,b) != None:
    suma = suma(a,b)

    for filas in suma:
        print('[',end=' ')
        for elemento in filas:
            print(elemento, end=' ')
        print(']')
else:
    print('Las dimensiones no son las mismas, no se pueden sumar.')





