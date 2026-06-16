#Linear Search means searching element one by one until target element is found
#Algorithm
'''1.Start from the first element.
2.Compare current element with the target.
3.If it matches, return the index.
4.If not, move to the next element.
5.If we reach the end, the element is not present.'''

#implementation
arr=list(map(int,input().split()))#[10, 25, 7, 40, 15]
target=int(input())#40
for i in range(len(arr)):
    if arr[i]==target:
        print("Element found at index",i)#Element found at index 3
        break
else:
    print("Element not found")

#using functions
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=list(map(int,input().split()))
target=int(input())
result=linear_search(arr,target)
print(result)