def first_occ(arr,target):
    n=len(arr)
    left=0
    right=n-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
          ans=mid
          right=mid-1
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return ans
arr=list(map(int,input().split()))
target=int(input())
result=first_occ(arr,target)
print(result)

#last occurence
def last_occ(arr,target):
    n=len(arr)
    left=0
    right=n-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
          ans=mid
          left=mid+1
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return ans
arr=list(map(int,input().split()))
target=int(input())
result=last_occ(arr,target)
print(result)

