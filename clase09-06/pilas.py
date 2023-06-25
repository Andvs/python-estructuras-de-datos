'''
Pilas
una pila de datos(stack en inglés) es una estructura de datos en donde
el último elemento en entrar es el primero en salir siguiendo el principio LIFO
(last in, first out), es decir, último en entrar, primero en salir

ejemplo: es ir apilando datos, como si fuera una pila de platos

operaciones:
push: agrega un elemento al tope del stack
pop: elimina el elemento en el tope de la pila
peek o top: obtiene el valor del elemento en el tope del stack sin 
eliminarlo
size: obtiene la cantidad de elementos en el stack
isEmpty: verifica si la pila está vacía
isFull: verifica si el stack está lleno

'''

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)
    
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError('El stack está vacío')
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def top(self):
        if self.isEmpty():
            return 'El stack está vacío'
        else:
            return self.stack[-1]
    

pila = Stack()

pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
print(pila)

pila.pop()
pila.pop()
pila.pop()

print(pila)
print(pila.top())

pila.pop()
print(pila.isEmpty())
print(pila.top())