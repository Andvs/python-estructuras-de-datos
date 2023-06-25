estudiantes = {}

for i in range(3):
    nombre = input(f'ingrese el nombre del estudiante {i+1}: ')
    asignatura = input('Ingrese el nombre de la asignatura: ')
    nota_lab1 = float(input('Nota lab 1: '))
    nota_lab2 = float(input('Nota lab 2: '))

    ponderacion = nota_lab1 * 0.3 + nota_lab2 * 0.7

    estudiantes[i+1] = {
        'Nombre': nombre,
        'Asignatura': asignatura,
        'Nota Laboratorio N°1': nota_lab1,
        'Nota Laboratorio N°2': nota_lab2,
        'Promedio final': round(ponderacion, 1)
    }

for estudiante in estudiantes.values():
    print('Información del estudiante:')
    for clave,valor in estudiante.items():
        print(f'{clave}: {valor}')


