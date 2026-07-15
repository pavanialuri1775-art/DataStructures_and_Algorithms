#2 radixsort:it is a non comparision based sorting algorithm which sort numbers ,digit by digit
def counting_sort(arr,place):
    n=len(arr)
    output=[0]*n
    count=[0]*10
    #counting frequnecy of digits
    for num in arr:
        index=(num//place)%10
        count[index]+=1
    #prefix sum
    for i in range(1,10):
        count[i]+=count[i-1]
    #travesring the array from right to left
    for i in range(n-1,-1,-1):
        index=(arr[i]//place)%10
        output[count[index]-1]=arr[i]
        count[index]-=1
    #copy back
    for i in range(n):
        arr[i]=output[i]
def radix_sort(arr):
    max_ele=max(arr)
    place=1
    while max_ele//place>0:
        counting_sort(arr,place)
        place*=10
    return arr
arr=[170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))
    