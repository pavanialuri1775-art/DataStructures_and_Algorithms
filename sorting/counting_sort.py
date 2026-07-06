#counting sort
def counting_sort(arr):
    max_val=max(arr)
    count=[0]*(max_val+1)
    for num in arr:
        count[num]+=1
    j=0
    for i in range(len(count)):
        while count[i]>0:
            arr[j]=i
            j+=1
            count[i]-=1
    return arr
arr=list(map(int,input().split()))
print(counting_sort(arr))