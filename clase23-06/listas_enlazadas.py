'''
Listas enlazadas

Conocida también como lista ligada, es una colección de nodos enlazados entre sí, donde
cada nodo contiene un elemento de datos y una referencia al siguiente nodo en la 
secuencia.

En Python, una lista enlazada se puede implementar utilizando clases.


nodo: se compone de dos partes, una que tiene la información en sí y la segunda 
es un puntero, que su función es apuntar al siguiente nodo si es que existe.

dirección: tienen una sola dirección y que en conjunto forman una estructura 
de datos lineal. Este nodo puede determinar quien se encuentra después de él 
pero no puede determinar quien se encuentra antes

null: cada puntero apuntará al nodo siguiente y el puntero de la última lista 
como no tiene a donde apuntar entonces apuntará a nulo.

ventajas: 
-capacidad para agregar o eliminar elementos de forma eficiente 
en cualquier posición
-utilizan memoria de manera más eficiente en comparación con las listas de 
arrays estáticos
-crecen o se reducen de forma dinámica según sea necesario. Ideal cuando se desconoce 
la cantidad exacta de elementos que se almacenarán.

'''

class Nodo:
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente


class ListaSimple:
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
        while(temporal.siguiente is not None):
            temporal = temporal.siguiente
        return temporal.dato
    
    def imprimir(self):
        nodo = self.primero
        while nodo != None:
            print(nodo.dato, end=' => ')
            nodo = nodo.siguiente
        print('None')
    

s = ListaSimple()
s.agregar_al_frente(5)
s.agregar_al_final(8)
s.agregar_al_frente(9)
s.eliminar_nodo(8)
s.imprimir()







