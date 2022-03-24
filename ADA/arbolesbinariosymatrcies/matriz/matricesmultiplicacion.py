#Pedimos las filas y columnas de las matrices 
contador = 0
filas1 = int(input("Introduce el numero de filas de matriz A :"))
column1 = int(input("Introduce el numero de columnas de matriz A: "))
column2 = int(input("Introduce numero de columnas matriz B : "))

##crear la matriz 1


A= []
for i in range(filas1):
    A.append([0]*column1)
    contador+=1

print("Crear matriz A : ")
for i in range(filas1):
    contador+=1
    print(A[i])


#Crear matriz 2
print("Crear Matriz B :")
B=[]
for i in range(column1):
    contador+=1
    B.append([0]*column2)


for i in range(column1):
    contador+=1
    print(B[i])

##cambiar valores de matriz 1

for i in range(filas1):
    for j in range(column1):
        contador+=1
        A[i][j] = float(input("Introduce el componente(%d,%d) de matriz A  : " % (i,j)))
print("----------------------")  
print("Matriz A :")
print("----------------------")
for i in range(filas1):
    contador+=1
    print(A[i])

##igual que en la primera matriz se cambian los valores de la segundo matriz xd
for i in range(column1):
    contador+=1
    for j in range(column2):
        B[i][j] = float(input("Introduce el componente(%d,%d) de matriz B : " % (i,j)))
        contador+=1
print("----------------------")      
print("Matriz B :")
for i in range(column1):
    contador+=1
    print(B[i])


print("-----------------------")
##crear el resultado en matriz con arrays
print("Calulando el valor de multiplicacion de matriz A y B")
print("-----------------------")
C = []
for i in range(filas1):
    contador+=1
    C.append([0]*column2)
for i in range(filas1):
    contador+=1
    print(C[i])

    #crear la multiplicacion despues de que se hcieron las matrices
    #C[i][j] + = A[i][k]*B[k][j]

    ##multiplicar matriz 1 y 2

for i in range(filas1):
    for j in range(column2):
        for k in range(column1):
            C[i][j] += A[i][k] * B[k][j]
            contador+=3



##sacar las nuevas matrices resultado- final
 
for i in range(filas1):
    R=[]
    for j in range(column2):
        contador+=2
        R.append(C[i][j])    
print("Resultado final : " , R)
print("Numero de instrucciones al realizar el código :", contador)
