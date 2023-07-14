'''

LISTAS CIRCULARES
Esta estructura es quella donde es el último nodo de la lista contiene una 
referencia al primero, y puede ser recurrida infinitamente.

Esto significa que el siguiente elemento después del último elemento de la lista 
es el primer elemento de la lista, y el elemento anterior al primer elemento es el 
último elemento de la lista.

Ventajas 
se puede recorrer la lista desde cualquier punto y seguir iterando a través de los 
elementos hasta regresar al punto de partida. Útil en aplicaciones donde se requiere un acceso 
continuo y repetido a los elementos de la lista.

Los nodos que existen pueden reutilizarse en lugar de crear nuevos nodos.
Esto puede ser beneficiosos en términos de eficiencia de memoria.

La implementación de esta listas es simple. Los enlaces entre los nodos son directos y no reuqieren 
una lógica compleja de punteros o referencias.

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class ListaCircular:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            #si el siguiente nodo del nodo actual es el nodo principal, significa que
            # este nodo es el nodo de cola.
            #si no, mueva el puntero hacia atrás
            if cur.next == self.head:
                break
            else:
                cur = cur.next
        return count
    
    def travel(self):
        if self.is_empty():
            return
        cur = self.head
        print(cur.data)
        while cur.next != self.head:
            cur = cur.next
            print(cur.data)
    
    def add_first(self, data):
        #agregar un nodo en la cabeza
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            #mueva el puntero al nodo de cola
            while cur.next is not self.head:
                cur = cur.next
                #El nodo de cola paunta al nuevo nodo
            cur.next = node
                #El nuevo nodo apunta al nodo principal original
            node.next = self.head
                #Luego dele el título del nodo principal al nuevo nodo
            self.head = node
            
    def add_last(self, data):
        #agregar un nodo al final
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            #mueve el puntero al final
            while cur.next is not self.head:
                cur = cur.next
                #el nodo de cola apunta al nuevo nodo
            cur.next = node
                #el nuevo nodo apunta al nodo principal
            node.next = self.head

    def insert_node(self, index, data):
        #insertar un nodo en una posición especifíca
        node = Node(data)
        if index < 0 or index > self.length():
            print('Posición de inserción incorrecta')
            return False
        elif index == 0:
            self.add_first(data)
        else:
            cur = self.head
            pre = None # pre es el nodo anterior del nodo señalado por el puntero actual
            count = 0
            #mueva el puntero a la posición para insertar
            while count < index:
                pre = cur
                cur = cur.next
                count += 1
            pre.next = node
            node.next = cur

    def remove_node(self, data):
        #eliminar nodo especificado
        if self.is_empty():
            return
            #si el nodo que se va a eliminar es el nodo principal
        elif data == self.head.data:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            pre = None
            #mover a la posición del nodo que se va a eliminar
            while cur.data != data:
                pre = cur
                cur = cur.next
                #Apunte el nodo precursor del nodo que se va a eliminar al nodo
                #posterior, de modo que se omita el nodo central

            pre.next = cur.next
    
    def is_exist(self, data):
        #buscar si el nodo especificado existe
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
                #La cola ha sido encontrada
            elif cur.next == self.head:
                return False
            else:
                cur = cur.next
        return False
    

lista_circular = ListaCircular()
lista_circular.add_last(2)
lista_circular.add_first(1)
lista_circular.add_first(0)
lista_circular.add_last(3)
lista_circular.insert_node(2,8)
lista_circular.travel()
print(f'La longitud de la lista: {lista_circular.length()}')
lista_circular.remove_node(8)
lista_circular.travel()
print(lista_circular.is_exist(2))
        
            


        
