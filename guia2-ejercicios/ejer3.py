# Desarrollar un programa para realizar operaciones estadísticas básicas sobre una serie de
# datos. Implementar una lista enlazada simple para almacenar los datos y proporciona las
# siguientes funcionalidades:
# A. Agregar datos: Permite ingresar un nuevo dato a la lista.
# B. Calcular media: Calcula y devuelve la media (promedio) de los datos almacenados
# en la lista.
# C. Calcular desviación estándar: Calcula y devuelve la desviación estándar de los
# datos almacenados en la lista.
# D. Imprimir lista: Muestra en pantalla los datos almacenados en la lista.
# E. Verificar si la lista está vacía: Devuelve un valor booleano que indica si la lista está
# vacía.

class Nodo:
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class ListaSimple:
    def __init__(self):
        self.primero = None
    
    def agregar_al_frente(self, dato):
        self.primero = Nodo(dato = dato, siguiente = self.primero)
    
    def esta_vacia(self):
        return self.primero == None
    
    def agregar_al_final(self, dato):
        if not self.primero:
            self.primero = Nodo(dato = dato)
            return
        temporal = self.primero
        while temporal.siguiente:
            temporal = temporal.siguiente
        temporal.siguiente = Nodo(dato = dato)

    def eliminar_nodo(self, busqueda):
        temporal = self.primero
        prev = None
        while temporal and temporal.dato != busqueda:
            prev = temporal
            temporal = temporal.siguiente
        if prev is None:
            self.primero = temporal.siguiente
        elif temporal:
            prev.siguiente = temporal.siguiente
            temporal.siguiente = None

    def obtener_ultimo_nodo(self):
        temporal = self.primero
        while(temporal.siguiente is not None):
            temporal = temporal.siguiente
        return temporal.dato
    
    def imprimir(self):
        nodo = self.primero
        while nodo != None:
            print(nodo.dato)
            nodo = nodo.siguiente
        

    def calcular_media(self):
        if not self.esta_vacia():
            nodo = self.primero
            lista_datos = []
            sum_datos = 0

            while nodo != None:
                lista_datos.append(nodo.dato)
                sum_datos += nodo.dato
                nodo = nodo.siguiente

            numero_datos = len(lista_datos)
            promedio = sum_datos/numero_datos
        
            return promedio
        else:
            print('La lista está vacía. No se puede realizar la operación.')

        

    def calcular_desviacion_estandar(self):
        #formula desviación estandar para población
        #((sumatoria (dato-media)**2)/numero de datos)**(1/2)
        if not self.esta_vacia():
            nodo = self.primero
            media = self.calcular_media()
            numero_datos = 0

            #sumatoria (dato-media)**2
            sumatoria = 0

            while nodo != None:
                operacion = (nodo.dato - media)**2
                sumatoria += operacion
                numero_datos += 1
                nodo = nodo.siguiente

            desviacion_estandar = (sumatoria/numero_datos)**(1/2)

            return desviacion_estandar
        else:
            print('La lista está vacía. No se puede realizar la operación.')

s = ListaSimple()
s.agregar_al_final(6)
s.agregar_al_final(2)
s.agregar_al_final(3)
s.agregar_al_final(1)
print('Datos almacenados:')
s.imprimir()

print(f'¿Esta la lista vacía?: {s.esta_vacia()}')
print(f'Media: {s.calcular_media()}')
print(f'Desviación estandar: {s.calcular_desviacion_estandar()}')




    


    

