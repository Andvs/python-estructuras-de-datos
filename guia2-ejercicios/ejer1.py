# Un equipo de desarrolladores tiene la misión de programar una aplicación de reproducción
# de música y se necesita implementar una lista enlazada doble para administrar la lista de
# reproducción de un usuario en específico. Cada nodo de la lista representa una canción, y
# cada canción tiene un título y un artista.
# Se solicita implementar una lista enlazada doble para una lista de reproducción de música.


class NodoCancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.siguiente = None
        self.anterior = None
    
class ListaReproduccion:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None
    
    def agregar_al_final(self, titulo, artista):
        nuevo_nodo = NodoCancion(titulo, artista)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        
    def agregar_al_inicio(self, titulo, artista):
        nuevo_nodo = NodoCancion(titulo, artista)
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
            print()
            print(f'Titulo: {actual.titulo}')
            print(f'Artista: {actual.artista}')
            actual = actual.siguiente

    def obtener_cabecera(self):
        return self.primero.titulo if self.primero else None
    
    def obtener_cola(self):
        return self.ultimo.titulo if self.primero else None
    
    def existe(self, busqueda):
        actual = self.primero
        while actual:
            if actual.titulo == busqueda:
                return True
            actual = actual.siguiente
        return False

    def eliminar_cancion(self, busqueda):
        actual = self.primero
        while actual:
            if actual.titulo == busqueda:
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


lista_reproduccion = ListaReproduccion()

lista_reproduccion.agregar_al_final('canción 1', 'artista 1')
lista_reproduccion.agregar_al_final('canción 2', 'artista 2')
lista_reproduccion.agregar_al_final('canción 3', 'artista 3')
lista_reproduccion.agregar_al_final('canción 4', 'artista 4')

lista_reproduccion.eliminar_cancion('canción 3')
lista_reproduccion.imprimir()

