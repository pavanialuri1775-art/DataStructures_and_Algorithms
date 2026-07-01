#1 in-place Quick sort
def partition(arr,low,high):#low-starting index,high-ending index
    pivot=arr[high]#last element as pivot
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def  quick_sort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
arr=list(map(int,input().split()))
quick_sort(arr,0,len(arr)-1)
print(arr)