#linear search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=list(map(int,input().split()))
target=int(input())
print(linear_search(arr,target))

#binary search
def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=list(map(int,input().split()))
target=int(input())
result=binary_search(arr,target)
print(result)


#bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))
result=bubble_sort(arr)
print(result)

#selectio sort
def  selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=list(map(int,input().split()))
result=selection_sort(arr)
print(result)

#Insertion sort
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

#quick  sort
def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[n//2]
    left=[]
    middle=[]
    right=[]
    for num in arr:
        if num<pivot:
            left.append(num)
        elif num==pivot:
            middle.append(num)
        else:
            right.append(num)
    return quick_sort(left)+middle+quick_sort(right)
arr=list(map(int,input().split()))
result=quick_sort(arr)
print(result)

#merge  sort
def  merge_sort(arr):
    n=len(arr)
    l=0
    r=n-1
    if n>1:
        mid=(l+r)//2
        left=arr[:mid+1]
        right=arr[mid+1:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return arr   
arr=list(map(int,input().split()))
result=merge_sort(arr)
print(result)
    