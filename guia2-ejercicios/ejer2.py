# Se está implementando un programa para administrar una cola de atención al cliente en
# una farmacia. Cada cliente tiene un número de ticket y un número de caja para que pueda
# ser atendido. Se solicita implementar un algoritmo que contenga una lista circular para
# manejar la cola de atención de tres cajas: Caja 1, Caja 2 y Caja 3.

class Nodo:
#se crea la clase nodo la cual crea la estructura de la lista y alamcena los datos
    def __init__(self , dato):

        self.dato = dato
        self.siguiente = None

class Listacircular:
#se crea la clase listacircular la cual representara el manejo de la cola de clientes entrando y saliendo de las cajas
    def __init__(self):

        self.primero = None
        self.ultimo = None
    
    def is_empty(self):
    #se verifica si la lista esta vacia
        return self.primero == None
    
    def agregar_cliente(self , dato):
    #se agrega un cliente en la primera posicion y luego detras del primero
        if self.is_empty():
        #si la lista esta vacia iguala el primer y ultimo "elemeneto" y se les aignara el valor del dato ingresado en 
        # la clase nodo y se realiza la conexion haciendo que el siguiente dato se conecte con el primero
            self.primero = self.ultimo = Nodo(dato)
            self.primero.siguiente = self.primero
        else:
        #si no esta vacia se crea un nuevo nodo el cual tenfra la posicion del ltimo elemento,luego el nuevo nodo avanzara 
        # una posicion crear un nuevo nodo vacio y se le asigna un dato,luego se conecta el nuevo nodo que es el ultimo
        # con el primero
            nuevo_nodo = self.ultimo
            self.ultimo = nuevo_nodo.siguiente = Nodo(dato)
            self.ultimo.siguiente=self.primero

    def eliminar_primer_cliente(self):
    # elimina el cliente ubicado en la posicion inicial de la lista
        if self.is_empty():
        #si esta vacia imprime el siguinte mensaje
            print("la lista esta vacia")
        elif self.primero == self.ultimo:
        #si solo hay un dato lo establece como none para eliminarlo
            self.primero = self.ultimo = None
        else: 
        #si hay mas de un dato se establece que el siguiente elemento sea el primero,y luego se conecta el ultimo 
        # elemento con el segundo que ahora sera el primero
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

class Cliente:
#se crea la clase cliente la cual recibe un numero de ticket y el numero de la caja
    def __init__(self , ticket , caja):

        self.ticket = ticket
        self.caja = caja

class Atencion(Listacircular):
#se crea un clase la cual hereda de lista circular y representa la atencion de los clientes
    def __init__(self):
    #se crean 3 cajas las culaes representan un lista circular individual
        self.caja1 = Listacircular()
        self.caja2 = Listacircular()
        self.caja3 = Listacircular()

    def asignar_cliente(self , cliente):
    #se asigna un cliente a una caja dependiento del numero que le toco 
        if cliente.caja == 1:
            self.caja1.agregar_cliente(cliente)
        elif cliente.caja == 2:
            self.caja2.agregar_cliente(cliente)
        elif cliente.caja == 3:
            self.caja3.agregar_cliente(cliente)
        else:
            print("Caja no válida")

    def atender_cliente(self):
    #se atiende a los clientes y se muestra un mesaje
        if not self.caja1.is_empty():
        #si la caja no esta vacia se elimina el primer cliente y atiende al siguiente 
            cliente = self.caja1.primero.dato
            self.caja1.eliminar_primer_cliente()
            print(f"Se esta atendendo al cliente con el ticket N°{cliente.ticket},en la caja N°{cliente.caja}")
        elif not self.caja2.is_empty():
        #si la caja no esta vacia se elimina el primer cliente y atiende al siguiente 
            cliente = self.caja2.primero.dato
            self.caja2.eliminar_primer_cliente()
            print(f"Se esta atendendo al cliente con el ticket N°{cliente.ticket},en la caja N°{cliente.caja}")
        elif not self.caja3.is_empty():
        #si la caja no esta vacia se elimina el primer cliente y atiende al siguiente 
            cliente = self.caja3.primero.dato
            self.caja3.eliminar_primer_cliente()
            print(f"Se esta atendendo al cliente con el ticket N°{cliente.ticket},en la caja N°{cliente.caja}")
        else:
        #si las cajas estan vacias ,se muestra el siguiente menaje
            print("No quedan clientes que atender")

cola = Atencion()

cliente1=Cliente(3,1)
cliente2=Cliente(1,2)
cliente3=Cliente(2,3)
cliente4=Cliente(1,3)
cliente5=Cliente(1,1)
cliente6=Cliente(1,3)
cola.asignar_cliente(cliente1)
cola.asignar_cliente(cliente2)
cola.asignar_cliente(cliente3)
cola.asignar_cliente(cliente4)
cola.asignar_cliente(cliente5)
cola.asignar_cliente(cliente6)
cola.atender_cliente()
cola.atender_cliente()
cola.atender_cliente()
cola.atender_cliente()
cola.atender_cliente()
cola.atender_cliente()

