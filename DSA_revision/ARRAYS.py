#Find the maximum element without using max().
#arr = [7, 2, 9, 4, 1, 8]
def max_ele(arr):
    maximum_element=float('-inf')
    for num in arr:
        if num>maximum_element:
            maximum_element=num
    return maximum_element
arr=list(map(int,input().split()))
print(max_ele(arr))
#time complexity--O(n)
#Space complexity--O(1)

#second largest
def sec_max(arr):
    fst_max=float('-inf')
    sec_max=float('-inf')
    for num in arr:
        if num>fst_max:
            sec_max=fst_max
            fst_max=num
        elif num>sec_max and num!=fst_max:
            sec_max=num
    if sec_max==float('inf'):
        return None
    return sec_max
arr=list(map(int,input().split()))
print(sec_max(arr))
#time complexity--O(n)
#Space complexity--O(1)

#Reverse an Array
def reverse_arr(arr):
    new_lst=[]
    for i in range(len(arr)-1,-1,-1):
        new_lst.append(arr[i])
    return new_lst
arr=list(map(int,input().split()))
print(reverse_arr(arr))
#time complexity--O(n)
#space complexity--O(n) since i have created a new list

#to reduce the spacee complexity from O(n) to o(1) in reversing an array we use two pointers
def reverse_arr(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
arr=list(map(int,input().split()))
print(reverse_arr(arr))
#time complexity--O(n)
#space complexity--O(1)

#Problem: Move Zeroes
def Move_Zeroes(arr):
    left=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[left],arr[i]=arr[i],arr[left]
            left+=1
    return arr
arr=list(map(int,input().split()))
print(Move_Zeroes(arr))
#time complexity--0(n)
#space complexity--o(1)

#Remove Duplicates from Sorted Array
def remove_duplicates(arr):
    if len(arr)==0:
        return 0
    pos=1
    for i in range(1,len(arr)):
        if arr[i]!=arr[pos-1]:
            arr[pos]=arr[i]
            pos+=1
    return pos
arr=list(map(int,input().split()))
k=remove_duplicates
print(k)
print(arr[:k])

