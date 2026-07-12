#lomuto:selecting the last element as pivot
def lomuto(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j  in  range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if low<high:
        pi=lomuto(arr,low,high)#2
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
a=[50,20,60,10,40]
quick_sort(a,0,len(a)-1)
print(a)