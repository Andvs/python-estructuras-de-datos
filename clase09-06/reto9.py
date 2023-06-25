#ejercicio de pila
#Realizar un algoritmo que permita simular el proceso de apilar libros en una biblioteca, y
# luego ir sacándolos utilizando el principio de pilas. Utilizar clases y funciones.

class Pila:
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        return str(self.stack)
    
    def push(self, item):
        self.stack.append(item)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError('El stack está vacío')
    
    def size(self):
        return str(len(self.stack))
    
    def top(self):
        if self.isEmpty():
            return 'El stack está vacío'
        else:
            return self.stack[-1]

# pilaLibros = Pila()
# pilaLibros.push('Ciencias sociales I')
# pilaLibros.push('El arte de la guerra')
# pilaLibros.push('El quijote de la mancha')

# print(pilaLibros)

# pilaLibros.pop()
# pilaLibros.pop()
# print(pilaLibros)
# print(pilaLibros.top())
# pilaLibros.pop()
# print(pilaLibros.top())
# print(pilaLibros)
    

# EJERCICIO DE COLA
# Realizar un algoritmo que permita simular el proceso de atención en un banco. Se debe crear
# una lista con los nombres de los clientes. Utilizar clases y funciones.

class Cola:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)
    
    def estaVacia(self):
        return len(self.items) == 0
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if self.estaVacia():
            raise ValueError('La cola esta vacía')
        else:
            return self.items.pop(0)
        

colaBanco = Cola()
colaBanco.encolar('Vincent Van Gogh')
colaBanco.encolar('Pablo Picasso')
colaBanco.encolar('Leonardo Da vinci')
colaBanco.encolar('Salvador Dalí')
print(colaBanco)
colaBanco.desencolar()
print(colaBanco)


