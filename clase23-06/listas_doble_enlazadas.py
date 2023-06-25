'''
Listas enlazadas bidireccionales

también conocidas como listas doblemente enlazadas, son una 
variante de las listas enlazadas simples en las que cada nodo 
tiene una referencia tanto al nodo siguiente como al nodo anterior.

La navegación en este tipo de lista puede realizarse en ambas direcciones: hacia 
adelante y hacia atrás.

Ventajas: 
-La capacidad de navegar tanto hacia adelante como hacia atrás en la lista 
permite realizar búsquedas eficientes en ambas direcciones.
-Las operaciones de inserción y eliminación, son más eficientes en comparación con las 
listas enlazadas simples. Esto porque no es necesario recorrer la lista para encontrar el 
nodo anterior o realizar ajustes en los enlaces.
-como cada nodo tiene una referencia al nodo anterior. es posible revertir rápidamente 
el orden de los en la lista sin tener que reconstruir la estructura.


'''

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
    
class ListaDoblementeEnlazadas:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None
    
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        
    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo

    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def obtener_cabecera(self):
        return self.primero.dato if self.primero else None
    
    def obtener_cola(self):
        return self.ultimo.dato if self.primero else None
    
    def existe(self, busqueda):
        actual = self.primero
        while actual:
            if actual.dato == busqueda:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, busqueda):
        actual = self.primero
        while actual:
            if actual.dato == busqueda:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior
                break
            actual = actual.siguiente
    
    

s = ListaDoblementeEnlazadas()
s.agregar_al_inicio(1)
s.agregar_al_inicio(2)
s.agregar_al_inicio(3)
s.agregar_al_inicio(4)
s.imprimir()

