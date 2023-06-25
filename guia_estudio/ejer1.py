# 1. Crear una lista de diccionarios llamada pacientes donde cada diccionario representa a
# un paciente con su informacion personal. Se solicita crear una lista de 4 diccionarios. ´
# Agregar la informacion mediante teclado. La informaci ´ on personal de cada paciente es: ´
# a) Nombre (tipo String)
# b) Edad (tipo Int)
# c) Peso (tipo Float)
# d) Sintomas (Lista de String)
# Ademas realizar una b ´ usqueda en la lista de pacientes para encontrar un paciente en ´
# espec´ıfico por nombre y mostrar su ficha personal correspondiente.

pacientes = []

for i in range(4):
    paciente = {}
    nombre = input('Nombre: ')
    edad = int(input('Edad: '))
    peso = float(input('Peso: '))
    num_sintomas = int(input('numero de sintomas: '))
    sintomas = []
    
    for i in range(num_sintomas):
        sintoma = input(f'Sintoma {i+1}: ')
        sintomas.append(sintoma)

    pacientes.append(dict(Nombre = nombre, Edad = edad, Peso = peso, Sintomas = sintomas ))


busqueda = input('Ingresa el nombre de un paciente para mostrar su ficha personal: ')

for paciente in pacientes:
    if busqueda in paciente.values():
        for x,y in paciente.items():
            print(f'{x}: {y}')

