# variable sliding window:window size varies
def vari_sliding(arr,k):
    left=0
    max_len=0
    total=0
    for right in range(len(arr)):
        total+=arr[right]
        while total>k:
            total-=arr[left]
            left+=1
        max_len=max(max_len,right-left+1)
    return max_len
arr=list(map(int,input().split()))
k=int(input())
print(vari_sliding(arr,k))  

