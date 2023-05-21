import 'dart:math';
// Multiplicar las siguientes dos listas de 5 elementos cada una.
// a: [4,3,2,2,1]
// b: [-3,2,8,0,1]
// La lista que se obtenga se debe concatenar con una nueva lista de 5 elementos aleatorios
// (numeros negativos random de -1 al - 5). Luego ordenar la lista de forma descendente.


void main() {
  List<int> a = [4,3,2,2,1];
  List<int> b = [-3,2,8,0,1];
  List<int> multi_ab = [];
  Random random = Random();
  List<int> lista_random = [];
  int elemento;

  // Multiplicar elemento a elemento entre la lista a y b
  for (int i = 0; i < 5; i++) {
    elemento = a[i]*b[i];
    multi_ab.add(elemento);
  }
  
  // crear lista de cinco elementos aleatorios de -1 al -5

  for (int i = 0; i < 5; i++) {
    // se añade elemento random a lista_random. se multiplica por -
    // para que el numero este entre el rango -1 al -5
    lista_random.add(-(random.nextInt(5) +1));
  }

  List<int> lista_concatenada = multi_ab + lista_random;
  print('Lista a: $a');
  print('Lista b: $b');
  print('Lista resultado multiplicación lista a y b: $multi_ab');
  print('Lista random: $lista_random');
  print('Lista concatenada: $lista_concatenada');

    //ordenar lista de forma descendente
  lista_concatenada.sort((a, b) => b.compareTo(a));
  print('Lista concatenada ordenada descendentemente: $lista_concatenada');

  





}