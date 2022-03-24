#Daniel Alejandro Morales Castillo 
#Materia de ADA
#Programa Python para la implementación de Insertion Sort
contador = 0
# Funcion de ordenamietno por Insercion
def insertionSort(arr): 

	# Atraviesa 1 hasta len (arr)
	for i in range(1, len(arr)): 
		key = arr[i] 
		#Mover elementos de arr [0..i-1], que son
		#mayor que la clave, a una posición por delante
		#de su posición actual
		j = i-1
		contador+=1
		while j >= 0 and key < arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
				contador+=2
		arr[j + 1] = key 


#Código de controlador para probar arriba
print("Numero de instrucciones" ,contador)
arr = [44, 34,7, 25, 12,10,22,11, 9,5,50]
insertionSort(arr) 
for i in range(len(arr)): 
	print ("% d" % arr[i])


