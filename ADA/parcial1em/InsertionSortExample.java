public class InsertionSortExample {//Abre Clase
    static int contador=0;
    public static void main(String a[]){//Abre Main
         // int arr[] ={ 26, 201, 210, 12, 266, 99, 118, 154, 177, 92, 223, 221, 90, 5, 258, 194, 110, 152, 220, 41, 163, 161, 21, 18, 247, 263, 164, 190, 205, 104, 4, 22, 254, 85, 284, 123, 83, 45, 265, 89, 252, 283, 236, 119, 96, 290, 29, 127, 138, 300, 175, 182, 270, 98, 48, 273, 59, 264, 148, 135, 102, 35, 37, 217, 57, 15, 73, 294, 39, 199, 146, 100, 267, 202, 56, 248, 55, 198, 162, 38, 285, 8, 232, 112, 200, 178, 246, 187, 240, 115, 228, 125, 6, 124, 176, 107, 86, 108, 253, 10, 116, 249, 94, 65, 288, 214, 251, 155, 260, 143, 69, 281, 68, 106, 50, 117, 58, 185, 156, 71, 72, 66, 132, 33, 16, 139, 168, 166, 227, 52, 88, 149, 140, 121, 34, 122, 189, 158, 159, 144, 188, 93, 70, 145, 153, 78, 142, 279, 167, 151, 282, 259, 216, 165, 47, 170, 54, 64, 147, 239, 184, 28, 173, 280, 183, 203, 255, 287, 126, 222, 136, 141, 218, 242, 275, 133, 49, 101, 196, 244, 91, 105, 43, 206, 19, 2, 128, 30, 245, 169, 181, 229, 256, 204, 271, 208, 25, 113, 274, 215, 272, 131, 46, 67, 207, 211, 51, 289, 235, 278, 193, 230, 291, 3, 174, 171, 276, 226, 114, 79, 61, 299, 224, 9, 75, 137, 257, 31, 157, 87, 292, 74, 268, 225, 62, 233, 53, 17, 7, 286, 262, 191, 241, 160, 212, 27, 129, 120, 298, 63, 14, 186, 237, 111, 219, 261, 76, 97, 231, 293, 238, 36, 13, 103, 32, 95, 269, 192, 42, 82, 130, 77, 197, 24, 84, 250, 134, 213, 195, 243, 295, 209, 297, 44, 60, 180, 40, 179, 11, 172, 150, 277, 81, 234, 23, 1, 296, 109, 20, 80
        int arr[] = {64, 45, 57,86,12     
    };
        System.out.println("Antes de Insertion Sort");
        for(int i:arr){
            System.out.print(i+" ");
        }
        System.out.println();

        insertionSort(arr);//sorting array using insertion sort

        System.out.println("Despues de Insertion Sort");
        for(int i:arr){
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
