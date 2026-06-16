
#insertion sort:Insertion Sort is a simple sorting algorithm that builds the final sorted array one element at a time.

#algorithm
'''1. consider 1st ele as sorted
2.2nd element=key
3.compare key ele with  elements 
4.insert if key<prev  ele ,shift right
5.repeat'''
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
result=insertion_sort(arr)
print(result)
