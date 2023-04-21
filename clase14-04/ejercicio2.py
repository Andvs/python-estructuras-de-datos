# Crear un algoritmo que permita guardar los nombres y el RUT de 5
# personas sin perder ninguna de ellas. El usuario tiene que ingresar la
# información de cada persona por consola. Se debe imprimir los
# arrays de nombres y RUT para luego ordenarlas alfabéticamente y
# ascendentemente respectivamente.

lista_rut = []
lista_nombres = []
for i in range(5):
    nombre= input('Nombre: ')
    rut = input('Rut: ')
    lista_nombres.append(nombre)
    lista_rut.append(rut)


print('Nombres en orden alfabetico: ')
print(sorted(lista_nombres))
print('Ruts en orden ascendente:')
print(sorted(lista_rut))





