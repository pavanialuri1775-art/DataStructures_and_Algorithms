#Reverse an Array
arr=list(map(int,input().split()))
left=0
right=len(arr)-1
while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
print(arr)

#Check whether a string is a palindrome
s=input()
left=0
right=len(s)-1
while left<right:
    if s[left]!=s[right]:
        print("false")
        break
    left+=1
    right-=1
else:
    print("True")
    
#Move all zeros to the end while maintaining the order of the non-zero elements.
arr=list(map(int,input().split()))
left=0
for j in range(len(arr)):
    if arr[j]!=0:
        arr[left],arr[j]=arr[j],arr[left]
        left+=1
print(arr)

#Remove Duplicates from a Sorted Array
arr=list(map(int,input().split()))
left=1
for right in range(1,len(arr)):
    if arr[right]!=arr[left-1]:
        arr[left]=arr[right]
        left+=1
print(arr[:left])

#Pair Sum in a Sorted Array
def two_pointers(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        s=arr[left]+arr[right]
        if s==target:
            return [arr[left],arr[right]]
        elif s<target:
            left+=1
        else:
            right-=1
    return -1
arr=list(map(int,input().split()))
target=int(input())
print(two_pointers(arr,target))
    
#merge two sorted arrays
a=list(map(int,input().split()))
b=list(map(int,input().split()))
left=0
right=0
res=[]
while left<len(a) and right<len(b):
    if a[left]<b[right]:
        res.append(a[left])
        left+=1
    else:
        res.append(b[right])
        right+=1
while left<len(a):
    res.append(a[left])
    left+=1
while right<len(b):
    res.append(b[right])
    right+=1
print(res)
        
        

