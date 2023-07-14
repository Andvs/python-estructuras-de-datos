'''
Realizar un algoritmo que permita simular una lista enlazada que permita agregar frutas. Se
debe crear un menú que llame las siguientes funciones:
A) Agregar un fruta al final de la lista
B) Agregar una fruta al inicio
C) Eliminar una fruta
D) Imprimir la lista actual
E) Obtener cabecera
F) Obtener cola

'''

class Nodo:
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None
    
    def agregar_al_frente(self, dato):
        self.primero = Nodo(dato = dato, siguiente = self.primero)
    
    def esta_vacia(self):
        return self.primero == None
    
    def agregar_al_final(self, dato):
        if not self.primero:
            self.primero = Nodo(dato = dato)
            return
        temporal = self.primero
        while temporal.siguiente:
            temporal = temporal.siguiente
        temporal.siguiente = Nodo(dato = dato)
    
    def eliminar_nodo(self, busqueda):
        temporal = self.primero
        prev = None
        while temporal and temporal.dato != busqueda:
            prev = temporal
            temporal = temporal.siguiente
        if prev is None:
            self.primero = temporal.siguiente
        elif temporal:
            prev.siguiente = temporal.siguiente
            temporal.siguiente = None

    def obtener_ultimo_nodo(self):
        temporal = self.primero
        while temporal.siguiente is not None:
            temporal = temporal.siguiente
        return temporal.dato
    
    def imprimir(self):
        nodo = self.primero
        while nodo != None:
            print(nodo.dato, end=' => ')
            nodo = nodo.siguiente
        print('None')


    

frutas = ListaEnlazada()

while True:
    print()
    print('1) Agregar una fruta al final de la lista')
    print('2) Agregar una fruta al inicio')
    print('3) Eliminar una fruta')
    print('4) Imprimir la lista actual')
    print('5) Obtener cabecera')
    print('6) Obtener cola')
    print('7) salir')
    print()

    while True:
        try:
            opcion = int(input('Escoge una accion, escribe el correspondiente número: '))
            if type(opcion) == int and 1 <= opcion <= 7:
                break
            else:
                print('Intenta otra vez. Un número entre 1 y 7.')
        except:
            print()
            print('Ingresa un número. Entre 1 y 7.')

    
    if opcion == 1:
        fruta = input('Fruta para agregar al final: ')
        frutas.agregar_al_final(fruta)
    elif opcion == 2:
        fruta = input('Fruta para agregar al frente: ')
        frutas.agregar_al_frente(fruta)
    elif opcion == 3:
        fruta = input('Fruta para eliminar: ')
        frutas.eliminar_nodo(fruta)
    elif opcion == 4:
        print()
        frutas.imprimir()
        print()
    elif opcion == 5:
        print()
        print(frutas.primero.dato)
    elif opcion == 6:
        print(frutas.obtener_ultimo_nodo())
    else:
        break


    






    

