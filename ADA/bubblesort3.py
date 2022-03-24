import random
from time import time 

def llenar():
    arr = []
    for m in range(100):
        arr.append(random.randint(1,1000))
    print("Lista desordenada", arr)
    ordenar(arr)

def ordenar(arr):
    incio = time()
    band = False
    while band == False:
        band = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i +  1]:
                aux = arr[i]
                arr[i] = arr [i+1]
                arr[i + 1] = aux
                band = False
    final = time() - incio
    print("*************")
    print("Lista areglada")
    print(arr)
    print(final, 's')


llenar()
