#1 Find an element in sorted array
'''def binary_search(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=list(map(int,input().split()))
target=int(input())
result=binary_search(arr,target)
print(result)'''

#Count occurrences of a target
def binary_search(nums,target):
    count=0
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    count+=1
arr=list(map(int,input().split()))
target=int(input())
result=binary_search(arr,target)
print(result)