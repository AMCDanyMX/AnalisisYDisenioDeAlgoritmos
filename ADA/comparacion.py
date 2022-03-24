
def create_array(size=10,max=50):
    from random import randint
    return[randint(0,max) for _ in range(size)]


def bubble_sort(arr):
    swapped=True
    while swapped:
        swapped=False
        for i in range(1,len(arr):
            if arr[i-1]>arr[i]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                swapped=True
    return arr


def insertion_sort(a):
    for sort_len in range(1,len(a)):
        cur_item=a[sort_len]
        insert_idx=sort_len

        while insert_idx>0 and cur_item<a[insert_idx-1]:
            a[insert_idx]=a[insert_idx-1]
            insert_idx+=-1
        
        a[insert_idx]= cur_item
    return a


def benchmark(n=[10,100,100,10000]):    
    from time import time
    insertion_times=[]
    bubble_times=[]

    for size in n:
        a=create_array(size,size)

        t0=time()
        bubble_sort(a)
        t1=time()
        bubble_times.append(t1-t0)
        
        t0=time()
        insertion_sort(a)
        t1=time()
        insertion_times.append(t1-t0)

    print"\nn\tInsertion\tbubble
    print 50*" "
    for i , size in enumerate(n):
        print "d\t%0.5f    \t0.5f"%(
            size,
            insertion_times[i],
            bubble_times[i]
        )
    print "\n"

benchmark()