#Linear Search
#Given an array and a key, find whether the key exists in the array. If found, return its position; otherwise return -1.
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=list(map(int,input().split()))
key=int(input())
result=linear_search(arr,key)
print(result)
        