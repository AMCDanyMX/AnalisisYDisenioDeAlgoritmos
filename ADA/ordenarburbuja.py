from random import randint


def create_array(length=10,maxint=50):
    new_arr=[randint(0,maxint) for _ in range(length)]
    return new_arr

def bubble_sort(arr):
    swapped=True
    while swapped:
        swapped=False
    for i in range (1,len(arr)):
        if arr[i-1]>arr[i]:
            arr[i],arr[i-1]=arr[i-1],arr[i]
            swapped=True
    return arr

def is_sorted(arr):
    sorted_arr=sorted(arr)
    return arr==sorted_arr

def benchmark(n=[10,100,1000,10000]):
    from time import time

    b0=[]
    b1=[]
    for length in n:
        a=create_array(length,length)

        t0=time()
        s=sorted(a)
        t1=time()
        b1.append(t1-t0)

        t0=time()
        s=bubble_sort(a)
        t1=time()
        b0.append(t1-t0)

    print("n  \tBuilt-In\tBubble Sort")
    print("___________________________")
    for i,cur_n in enumerate(n):
        print "%d\t%0.5f \t%0.5f"%(cur_n[i],b1[i],b0[i])

benchmark()

