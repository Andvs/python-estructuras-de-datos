// Obtener el promedio de tres listas diferentes de 7 elementos cada una. Los elementos
// de estas listas se generan de forma aleatoria (elementos del 30 al 100). Guardar los
// promedios obtenidos en una nueva lista.
import "dart:math";

void main(){
  // creamos 3 listas vacias
  List <int> lista1 = [];
  List <int> lista2 = [];
  List <int> lista3 = [];
  // creamos una instancia para usar la clase random
  final random = Random();
  // agregamos a las listas numeros aleatorios entre 30 y 100
  int n = 7;
  for (int i = 0; i < n; i++) {
    lista1.add(random.nextInt(71)+30);
    lista2.add(random.nextInt(71)+30);
    lista3.add(random.nextInt(71)+30);
    }
  // calculamos la suma de los elementos contenidos en la primera lista
  int suma1=0;
  for (int i = 0; i < n; i++) {
    suma1 = suma1 + lista1[i];
    }
  // calculamos la suma de los elementos contenidos en la segunda lista
  int suma2=0;
  for (int i = 0; i < n; i++) {
    suma2 = suma2 + lista2[i];
    }
  // calculamos la suma de los elementos contenidos en la tercera lista
  int suma3=0;
  for (int i = 0; i < n; i++) {
    suma3 = suma3 + lista3[i];
    }
  //obtenemos el promedio de cada lista dividendo las sumas realizadas anteriormente
  // por el numero de elementos en la lista
  double promedio1 = suma1/n;
  double promedio2 = suma2/n;
  double promedio3 = suma3/n;
  // creamos la lista vacía que almacenara los promedios
  List <double> promedios = [];
  // agregamos los promedios a la lista
  promedios.add(promedio1);
  promedios.add(promedio2);
  promedios.add(promedio3);

  print("la primera lista es :\n$lista1");
  print("la segunda lista es :\n$lista2");
  print("la tercera lista es :\n$lista3");
  print("el promedio la primera lista es :\n$promedio1");
  print("el promedio la segunda lista es :\n$promedio2");
  print("el promedio la tercera lista es :\n$promedio3");
  print("Los promedios obtenidos son:\n$promedios");
}