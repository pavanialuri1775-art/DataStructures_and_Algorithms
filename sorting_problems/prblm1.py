#Implement bubble sort
def bubble_sort(arr):
    n=len(arr)#5
    for i in range(n):#5
        for j in range(n-i-1):#1
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))
print(bubble_sort(arr))

#2 Optimized Bubble Sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

#Descending order
def bubble_sort(arr):
    n=len(arr)#5
    for i in range(n):#5
        for j in range(n-i-1):#1
            if arr[j+1]>arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))
print(bubble_sort(arr))

#count swaps
def bubble_sort(arr):
    n=len(arr)
    swaps_count=0
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaps_count+=1
    return swaps_count
arr=list(map(int,input().split()))
print(bubble_sort(arr))

#print array after every pass
def bubble_sort(arr):
    n=len(arr)#5
    for i in range(n):#5
        for j in range(n-i-1):#1
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)
    return arr
arr=list(map(int,input().split()))
bubble_sort(arr)

#Bubble sort strings
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if  arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(str,input().split()))
print(bubble_sort(arr))

