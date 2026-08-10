# Binary search 
def binary_search(nums,target):
    left=0                      
    right=len(nums)-1#4
    while left<=right:#3<=4
        mid=(left+right)//2#2#3
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1#3
        else:
            right=mid-1
    return -1
arr=list(map(int,input().split()))
target=int(input())
result=binary_search(arr,target)
print(result)