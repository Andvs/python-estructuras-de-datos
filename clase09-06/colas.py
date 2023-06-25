'''
Colas(filas)
Una cola actúa como una colección de objetos lineales que solo permiten insertar
por un extremo y eliminar por el contrario.
Así, el primer elemento añadido es el primero en ser eliminado. La cola 
es una estructua de tipo FIFO (first in First Out), es decir, el primero en estrar
primero en salir

ejemplo: las colas de personas en un banco. Las colas crecen hacia atrás, 
a medida que van llegando personas la cola se hace más grande, y l aprimera persona
que esté en la cola, será la primera en ser atendida.

operaciones:
encolar: agrega elementos al final de la cola.
desencolar: elimina elementos al principio de la cola..
isEmpty: verifica si la cola está vacía.
isfull: verifica si la fila está llena



'''

class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, x):
        self.items.append(x)
    
    def desencolar(self):
        if self.esta_vacia():
            raise ValueError('La cola esta vacía')
        return self.items.pop(0)
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)
    
cola = Cola()

cola.encolar('persona 1')
cola.encolar('persona 2')
cola.encolar('persona 3')
cola.encolar('persona 4')

print(cola)

print()

cola.desencolar()
cola.desencolar()
cola.desencolar()
cola.desencolar()

print(cola)

