#selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr    
arr=list(map(int,input().split()))
print(selection_sort(arr))

#sort the array in descending order
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]>arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr    
arr=list(map(int,input().split()))
print(selection_sort(arr))

#Print the array in every pass.
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        print(arr)
    return arr    
arr=list(map(int,input().split()))
selection_sort(arr)

#Print the index of the minimum element
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        print(f"minimum element= {arr[min_index]},Index={min_index}")
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr    
arr=list(map(int,input().split()))
selection_sort(arr)

#count the number of swaps
def selection_sort(arr):
    n=len(arr)
    swaps=0
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        swaps+=1
    return swaps    
arr=list(map(int,input().split()))
print(selection_sort(arr))

#count comparisions
def selection_sort(arr):
    n=len(arr)
    comparision_count=0
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            comparision_count+=1
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return comparision_count   
arr=list(map(int,input().split()))
print(selection_sort(arr))

#print the minimum element in every pass
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        print(arr[min_index])
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr  
arr=list(map(int,input().split()))
print(selection_sort(arr))

