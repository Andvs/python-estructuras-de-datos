// Crear una lista de caracteres y enteros como se muestra a continuacion: ´
// lista = [“a”, 2, 0, “b”, 8, “c”]
// Se solicita solo imprimir los numeros de la lista omitiendo los caracteres.


void main() {

  var lista = ['a', 2, 0, 'b', 8, 'c'];

  for (var i in lista) {
    if (i.runtimeType == int) {
      print(i);
    }
  }
}