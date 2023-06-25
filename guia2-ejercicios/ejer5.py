# 5. Se requiere gestionar una jerarquía de empleados en una empresa. Cada empleado tiene un
# cargo específico y puede tener uno o varios subordinados. Utilizando un árbol, elaborar el
# programa con las siguientes funcionalidades:
# A. Agregar empleado: Permite ingresar un nuevo empleado a la jerarquía. El
# empleado se agrega como subordinado de un empleado existente, especificando su
# cargo.
# B. Eliminar empleado: Elimina un empleado de la jerarquía, junto con todos sus
# subordinados. Al eliminar un empleado, todos sus subordinados pasan a ser
# subordinados del empleado superior.
# C. Mostrar la jerarquía: Muestra en consola la estructura jerárquica completa de la
# empresa, mostrando los empleados y sus respectivos subordinados en forma de
# árbol.
# D. Buscar empleado: Permite buscar un empleado en la jerarquía por su nombre y
# muestra su cargo y subordinados directos, si los tiene.
# E. Obtener jefe directo: Dado un empleado, muestra en pantalla el nombre y cargo de
# su jefe directo.

class Arbol:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


arbol = Arbol('a',
              Arbol('b',))
