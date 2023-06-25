# 3. Realizar un algoritmo utilizando la estructura de Pila en Python. Se desea almacenar el
# siguiente conjunto de documentos:
# documentos = [“Informe Final”, “Guia de Estudio”, “Tesis 4”, “Seminario Osorno”]
# a) Crear una funcion e imprimir el listado de documentos actual de la pila. ´
# b) Agregar el documento “Avance Tesis” y “Proyecto Integrador”.
# c) Obtener el ultimo elemento superior de la pila. ´
# d) Eliminar el documento de la parte superior.
# e) Imprimir la pila de documentos actualizadas.
# f) Verificar si esta vac´ıa la pila de documentos.

class Pila:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not(self.isEmpty()):
            return self.stack.pop()
        else:
            raise IndexError('La pila de documentos esta vacía')
    
    def size(self):
        return len(self.stack)
    
    def top(self):
        if self.isEmpty():
            return 'La pila de documentos esta vacía'
        else:
            return self.stack[-1]
        

documentos = Pila()

documentos.push('Informe final')
documentos.push('Guia de Estudio')
documentos.push('Tesis 4')
documentos.push('Seminario Osorno')
print(documentos)
documentos.push('Avance Tesis')
documentos.push('Proyecto Integrador')
print(documentos.top())
documentos.pop()
print(documentos)
print(documentos.isEmpty())



