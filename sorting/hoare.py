# hoare partition: hoare partition is a partition method in quick sort in which usually pivot selected as first element
def hoare(arr,low,high):
    piv = arr[low]
    i=low-1
    j=high+1
    while True:
        i+=1
        while arr[i]<piv:
            i+=1
        j-=1
        while arr[j]>piv:
            j-=1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]
def quick_sort(arr,low,high):
    if  low<high:
        pi=hoare(arr,low,high)
        quick_sort(arr,low,pi)
        quick_sort(arr,pi+1,high)
a=[50,20,60,10,40]
quick_sort(a,0,len(a)-1)
print(a)
        
            
            