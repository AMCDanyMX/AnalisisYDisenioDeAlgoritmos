public class InsertionSortExample {//Abre Clase
    static int contador=0;
    public static void main(String a[]){//Abre Main
        int[] arr1 = {};
        System.out.println("Antes de Insertion Sort");
        for(int i:arr1){
            System.out.print(i+" ");
        }
        System.out.println();

        insertionSort(arr1);//sorting array using insertion sort

        System.out.println("Despues de Insertion Sort");
        for(int i:arr1){
            System.out.print(i+" ");
        }
        System.out.println();
        System.out.println(contador + " instrucciones");
    }//Cierra Main

    public static void insertionSort(int array[]) {
        int n = array.length; //Se saca el tamaño del arreglo dado y se pone en n
        for (int j = 1; j < n; j++) { //Con este for recorremos el arreglo
            int key = array[j]; // Aqui guardamos el segundo numero del array,
                                //osea el que esta en la segunda posicion
                                //puesto que j = 1
            int i = j-1; // i sera siempre un numero menos que j
            while ( (i > -1) && ( array [i] > key ) ) { //Mientras i sea mayor a -1 y array[i]
                                                        //(que seria una posicion anterior a la posicion donde esta key)
                                                        //sea mayor a key se ejecutaran lo siguiente
                array [i+1] = array [i]; //Aqui copiamos el numero que estaba en la posicion i a la posicion i+1
                contador+=1;
                i--; //decrementamos i
            }
            array[i+1] = key; //una vez terminado el while se pone key en array[i+1], que se supone que fue el numero que recorrimos hacia atras
                              //hay que recordar que i se fue decrementando en while
            contador+=1;
        }
    }
}//Cierra Clase
