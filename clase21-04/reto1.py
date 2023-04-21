
palabra = input('Ingrese una palabra: ')
vocales = 'aeiouáéíóúüöäëï'
cont = 0
for i in palabra:
    if i in vocales:
        cont += 1

print(f'La palabra "{palabra}" tiene {cont} vocales.')
