import numpy
import sys 
print("Este programa hace la multiplicacion de matrices")
r1 = int(input("Introduce numero de renglones de matriz1: "))
c1 = int(input("Introduce numero de columnas de matriz1: "))
r2 = int(input("Introduce numero de renglones de matriz2: "))
c2 = int(input("Introduce numero de columnas de matriz2: "))

#verificar si se puede hacer la multiplicacion

if(c1 != r2):
    print("No se puede hacer la multiplicacion de matriz")
    sys.exit()

matriz1= numpy.zeros((r1,c1))
matriz2= numpy.zeros((r2,c2))
matrizr= numpy.zeros((r1,c2))
print("Introduce los elemtos de la matriz 1:  ")
for r in range(0,r1):
    for c in range(0,c1):
        matriz1[r,c]= input("Elemento a["+str(r+1)+str(c+1)+"]")
        
print("Introduce los elemtos de la matriz 2:  ")
for r in range(0,r2):
    for c in range(0,c2):
        matriz1[r,c]= input("Elemento a["+str(r+1)+str(c+1)+"]")
#operaciones de multiplicación
for i in range(0,r1):
    for c in range(0,c2):
        for k in range(0,r2):
            matrizr[r,c]+= matriz1[r,k]*matriz2[k,c]
print(matrizr)

            
        

