#Bubble Sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))#[5, 1, 4, 2, 8]
print(bubble_sort(arr))#[1,2,4,5,8]

#2  Selection Sort
def selection_sort(arr):
    n=len(arr)#5
    for i in range(n-1):
        min_index=i#0
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=list(map(int,input().split()))#64,25,12,22,11
print(selection_sort(arr))#[11,12,22,25,64]

#3 insertion sort
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=list(map(int,input().split()))
print(insertion_sort(arr))




            
    