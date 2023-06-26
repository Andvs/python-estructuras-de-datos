# Un supermercado necesita un programa para el manejo de un almacén de productos en una
# de sus sucursales. Los productos se reciben en una pila y se despachan en una cola para su
# entrega a los clientes. Se solicita implementar un algoritmo que incluya tanto el uso de pila y
# cola. Debe realizarse las siguientes operaciones:
# A. Agregar producto: Permite ingresar un nuevo producto al almacén. El producto se
# agrega a la pila de productos recibidos.
# B. Despachar producto: Remueve el producto más antiguo de la cola y lo entrega al
# cliente. Si la cola está vacía, muestra un mensaje indicando que no hay productos
# disponibles para despachar.
# C. Verificar si la pila de productos recibidos está vacía: Devuelve un mensaje que
# indica si la pila de productos recibidos está vacía.
# D. Verificar si la cola de productos para despachar está vacía: Devuelve un mensaje
# que indica si la cola de productos para despachar está vacía.
# E. Imprimir lista de productos recibidos: Muestra en consola los productos
# almacenados en la pila de productos recibidos.
# F. Imprimir lista de productos para despachar: Muestra en consola los productos
# almacenados en la cola de productos para despachar.
# G. Mostrar cantidad total de productos en el almacén: Muestra en consola la
# cantidad total de productos que hay en el almacén, sumando la cantidad de
# productos recibidos en la pila y la cantidad de productos para despachar en la cola.


class Pila:
# se crea la clase pila la cual representara la lista de productos_recibidos
    def __init__(self):
        self.productos = []

    def agregar(self,producto):
        self.productos.append(producto)

    def quitar(self):
        if not self.is_empty():
            self.productos.pop()
        else:
            raise ValueError("la pila productos estas vacia")
        
    def is_empty(self):
        return len(self.productos)==0
    
    def imprimir(self):
        print(self.productos)

class Cola:
#se crea la clase cola la cual representara la lista de productos_despacho
    def __init__(self):
        self.productos=[]

    def encolar(self,producto):
        self.productos.append(producto)

    def desencolar(self):
        if self.is_empty():
            raise ValueError("la cola esta vacia")
        return self.productos.pop()
    
    def is_empty(self):
        return len(self.productos)==0
    
    def imprimir(self):
        print(self.productos)

class Almacen:
    
    def __init__(self):
        self.productos_recibidos = Pila()
        self.productos_despacho = Cola()

    def agregar_producto(self,producto):
    #agrega un producto a self.productos_recibidos y a self.productos_despacho
        self.productos_recibidos.agregar(producto)
        self.productos_despacho.encolar(producto)

    def despachar_producto(self):
        #Despacha el ultimo elemento de productos_despacho
        if not self.productos_recibidos.is_empty():
            self.productos_despacho.desencolar()
        else:
            print("No hay productos disponibles para despachar")

    def productos_recibidos_is_empty(self):
    #si productos_Recibidos no tiene elementos devuelve un mensaje confirmandolo.
        if self.productos_recibidos.is_empty():
            print("La pila de productos recibidos está vacía")
 
    def productos_despacho_is_empty(self):
    #si productos_despacho no tiene elementos devuelve un mensaje confirmandolo.
        if self.productos_despacho.is_empty():
            print("La cola de productos para despachar está vacía")
    
    def imprimir_productos_recibidos(self):
    #imprime en un lista los elementos de productos_recibidos.
        self.productos_recibidos.imprimir()

    def imprimir_productos_despacho(self):
    #imprime en un lista los elementos de productos_despacho.
        self.productos_despacho.imprimir()

    def total_productos(self):
    # devuelve la cantidad de productos disponibles en el almacen
        productos_recibidos = len(self.productos_recibidos.productos)
        productos_despacho = len(self.productos_despacho.productos)
        total = productos_recibidos - productos_despacho

        if total >= 0:
            print(f"Hay {productos_despacho} productos ")
        else:
            print("No hay productos")
        
almacen = Almacen()
almacen.productos_recibidos_is_empty()
almacen.productos_despacho_is_empty()
almacen.agregar_producto("pan")
almacen.agregar_producto("gallatas")
almacen.agregar_producto("torta")
almacen.agregar_producto("carne")
almacen.agregar_producto("chocolate")
almacen.productos_recibidos_is_empty()
almacen.productos_despacho_is_empty()
print()
almacen.imprimir_productos_recibidos()
almacen.imprimir_productos_despacho()
print()
almacen.despachar_producto()

almacen.imprimir_productos_recibidos()
almacen.imprimir_productos_despacho()
print()
almacen.total_productos()









    
    