'''
2. Se necesita crear un sistema de gestión de tareas utilizando listas bidireccionales. Cada tarea
tiene un identificador único, un título, una descripción y un estado (pendiente, en progreso, o
completada). El sistema debe realizar las siguientes tareas:
A) Permitir agregar tareas
B) Eliminar tareas
C) Buscar una tarea en específico
D) Cambiar el estado de las tareas
E) Mostrar las tareas en orden ascendente según su identificador
Nota: Se solicita no solo implementar las funciones requeridas, sino también probarlas y mostrar los
resultados obtenidos anteriormente. Esto implica que se deben ejecutar las funciones con datos de
prueba o ejemplos específicos para demostrar su funcionamiento.
'''

class Nodo:
    def __init__(self, titulo, descripcion, estado, anterior = None):
        self.titulo = titulo
        self.siguiente = None
        self.anterior = anterior
        self.descripcion = descripcion
        self.estado = estado
    
class ListaBidireccional:
    def __init__(self):
        self.primero = None
    
    #agrega la tarea al final
    def agregar_tarea(self, titulo, descripcion, estado):
        if self.primero is None:
            self.primero = Nodo(titulo, descripcion, estado)
            return 

        temporal = self.primero
        prev = None

        while temporal.siguiente is not None:
            prev = temporal
            temporal = temporal.siguiente
        if temporal is None:
            return
        temporal = Nodo(titulo, descripcion, estado, anterior = prev)
    
    def eliminar_tarea(self, titulo):
        if self.primero and self.primero.titulo == titulo:
            self.primero = self.primero.siguiente
            return
    
        temporal = self.primero
        prev = None

        while temporal.siguiente and temporal.titulo != titulo:
            prev = temporal
            temporal = temporal.siguiente

        if temporal.titulo == None:
            return
        temporal.anterior = prev
        temporal = temporal.siguiente
        
    def imprimir_tareas(self):
    
        temporal = self.primero
        while temporal != None:
            print(temporal.titulo)
            temporal = temporal.siguiente
        

tareas = ListaBidireccional()
tareas.agregar_tarea('tarea 1', 'prueba en compu', 'en progreso')
tareas.agregar_tarea('tarea 2', 'prueba en compu', 'en progreso')
tareas.agregar_tarea('tarea 3', 'prueba en compu', 'en progreso')

tareas.imprimir_tareas()

#no funciona :C

        
        
        




    

    



    
