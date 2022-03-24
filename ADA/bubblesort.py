#Daniel Alejandro Morales Castillo 
#Materia de ADA
#Programa de implementacion de Bubble Sort 


def bubbleSort(arr):
    contador =0
    n = len(arr)
 
    # Recorre odos los elementos del arreglo
    for i in range(n):
        # Los ultimos elementos ya están en su lugar
        for j in range(0, n-i-1):
            contador+=1
            # atravesar la matriz de 0 a n-i-1
            # Cambiar si el elemento encontrado es mayor
            # que el siguiente elemento
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Numero de instrucciones ", contador)
 
#Código de controlador para probar lo de arriba
arr = [64, 45, 57,86,12]
print("Arreglo sin ordenar:", arr)
print("--------------------------")
bubbleSort(arr)
print ("El arreglo ordenado es :")
for i in range(len(arr)):
    print ("%d" %arr[i]), 