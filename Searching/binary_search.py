#Binary Search:
#Binary Search works only on a sorted array.
#Instead of checking every element one by one, we repeatedly divide the search space into half.

#Binary Search Algorithm
'''1.Find middle element.
2.Compare middle with target.
3.If equal → return index.
4.If target is smaller → search left half.
5.If target is larger → search right half.
6.Repeat until found or search space ends.'''

#code
'''arr=list(map(int,input().split()))
target=int(input())
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1'''
        
#using functions
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

    
        
     