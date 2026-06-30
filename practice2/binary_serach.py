#binary search
#Search for an element in a sorted array using Binary Search.
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
        