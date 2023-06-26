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

class Almacen:
    
    def __init__(self):
        self.pila_productos_recibidos = []
        self.cola_productos_para_despachar = []
    

    #cuando se agrega un producto, se agrega a la lista de recibidos, pero
    #a la vez, significa que es un producto que se puede despachar, por lo que
    #también se agrega a la lista de productos para despachar.

    def agregar_producto(self,producto):
        self.pila_productos_recibidos.append(producto)
        self.cola_productos_para_despachar.append(producto)

    #se verifica que la lista para despachar no este vacia, si lo
    #esta se imprime un mensaje que informe que no hay productos disponibles
    #para despachar.
    #de lo contrario se elimina el primero elemento de la lista

    def despachar_producto(self):
        if self.productos_despacho_is_empty():
            print("No hay productos disponibles para despachar")
        else:
            return self.cola_productos_para_despachar.pop(0)

    def productos_recibidos_is_empty(self):
        if len(self.pila_productos_recibidos)==0:
            print("La pila de productos recibidos está vacía")
 
    def productos_despacho_is_empty(self):
    
        if len(self.cola_productos_para_despachar)==0:
            print("La cola de productos para despachar está vacía")
    
    #la pila de productos recibidos funciona como un registro de los productos
    #agregados, por lo que también estan ordenados según van llegando.
    #por lo que esta lista no se va modificando, la lista de productos para
    #despachar es la unica en la que se eliminan los productos.

    def imprimir_productos_recibidos(self):
        print(f'Pila de productos recibidos: {self.pila_productos_recibidos}')

    def imprimir_productos_despacho(self):
        print(f'Cola de productos para despachar: {self.cola_productos_para_despachar}')

    #se cuentan los productos que hay en la cola, es decir, los productos que 
    #estan disponibles para despachar, ya que esos realmente representan los productos
    # que hay actualmente en el almacen. Ya que la pila de productos recibidos funciona
    # como un registro de todos los productos que se han agregado y no tiene sentido sumar las 
    # listas para obtener los productos que hay en el almacen.

    def total_productos(self):
        print(f'En el almacen hay actualmente un total de {len(self.cola_productos_para_despachar)} productos.')
        
almacen = Almacen()
almacen.productos_recibidos_is_empty()
almacen.productos_despacho_is_empty()
almacen.agregar_producto("pan")
almacen.agregar_producto("gallatas")
almacen.agregar_producto("torta")
almacen.agregar_producto("carne")
almacen.agregar_producto("chocolate")
almacen.imprimir_productos_recibidos()
almacen.imprimir_productos_despacho()
print('--------------------')
almacen.despachar_producto()
almacen.despachar_producto()
almacen.despachar_producto()
almacen.despachar_producto()
almacen.despachar_producto()
# almacen.despachar_producto()
print('-----------------------------')
almacen.imprimir_productos_recibidos()
almacen.imprimir_productos_despacho()

almacen.total_productos()






    
    