#Linear Search (Return All Occurrences)
def linear_search(arr,target):
    occ=[]
    for i in range(len(arr)):
        if arr[i]==target:
            occ.append(i)
    return occ
arr=list(map(int,input().split()))
target=int(input())
print(linear_search(arr,target))

#Count Number of Occurrences
def linear_search(arr,target):
    count=0
    for i in range(len(arr)):
        if arr[i]==target:
            count+=1
    return count
arr=list(map(int,input().split()))
target=int(input())
print(linear_search(arr,target))

#Find Maximum Element using Linear Search
def linear_search(arr):
    max_element=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_element:
            max_element=arr[i]
    return max_element
arr=list(map(int,input().split()))
print(linear_search(arr))

#Find Minimum Element
def linear_search(arr):
    min_element=arr[0]
    for i in range(len(arr)):
        if arr[i]<min_element:
            min_element=arr[i]
    return min_element
arr=list(map(int,input().split()))
print(linear_search(arr))