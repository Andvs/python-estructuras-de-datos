# 4. Desarrollar un algoritmo que contenga seis productos de supermercado utilizando colas
# con Python, implementando las siguientes funciones:
# a) Hacer un metodo que agregue un producto a la cola. ´
# b) Crear otro metodo para eliminar el primer producto de la cola. ´
# c) Otra funcion que muestre los productos en la cola sin modificar la cola, utilizando ´
# ciclos.
# d) Un metodo que invierta el orden de productos de la cola. ´
# e) Una funcion que elimine todos los productos de la cola

class Cola:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)
    
    def agregarProducto(self, item):
        self.items.append(item)
    
    def estaVacia(self):
        return len(self.items) == 0
    
    def eliminarProducto(self):
        if self.estaVacia():
            raise ValueError('La cola esta vacía')   
        else:
            return self.items.pop(0)
    
    def mostarProductos(self):
        for i in self.items:
            print(i)
        print()
    
    def vaciarCola(self):
        self.items.clear()
        

    #para invertir una lista se puede usar reverse() (modifica la lista original)
    #para invertir una lista se puede usar lista[::-1] (para crear una nueva lista invertida)
    def invertirOrden(self):
        self.items.reverse()

colaSuper = Cola()
colaSuper.agregarProducto('Pollo')
colaSuper.agregarProducto('Kilo de arroz')
colaSuper.agregarProducto('Un sable de luz')
colaSuper.mostarProductos()
colaSuper.eliminarProducto()
colaSuper.mostarProductos()


        


    