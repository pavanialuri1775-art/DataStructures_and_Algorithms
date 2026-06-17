#1
def find_index(arr,target):
    for index in range(len(arr)):
        if arr[index]==target:
            return index
    return -1
arr=list(map(int,input().split()))#[4, 8, 2, 9, 5]

target=int(input())#9
result=find_index(arr,target)
print(result)#3

##linear Traversal problems

#count how many times the target appears
def count_occurences(arr,target):
    count=0
    for index in range(len(arr)):
        if arr[index]==target:
            count+=1
    return count
    
arr=list(map(int,input().split()))#[2, 5, 2, 7, 2, 9]
target=int(input())#2
result=count_occurences(arr,target)
print(result)#3

#Find the maximum element in an array without using max().
def max_element(arr):
    largest_element=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest_element:
            largest_element=arr[i]
    return largest_element
arr=list(map(int,input().split()))
result=max_element(arr)
print(result)

#second largest element
def second_max(arr):
    fst_max=arr[0]
    sec_max=arr[1]
    if sec_max>fst_max:
        fst_max,sec_max=sec_max,fst_max
    for i in range(2,len(arr)):
        if arr[i]>fst_max:
            sec_max=fst_max
            fst_max=arr[i]
            
        elif arr[i]>sec_max:
            sec_max=arr[i]
    return sec_max
arr=list(map(int,input().split()))
result=second_max(arr)
print(result)
