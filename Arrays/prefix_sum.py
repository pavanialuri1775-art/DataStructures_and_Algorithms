#1 prefix_sum:A prefix sum stores the sum of all elements from the beginning up to the current index.
arr=list(map(int,input().split()))
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
left=int(input())
right=int(input())
if left==0:
    print(prefix[right])
else:
    print(prefix[right]-prefix[left-1])
    
#Longest subarray sum is k
def long_subarr(arr,k):
    pref_sum =0
    res_max = 0
    pref_map= {}
    for i in range(len(arr)):
        pref_sum+=arr[i]
        if pref_sum ==k:
            res_max = i+1
        if (pref_sum-k) in pref_map:
            length = i-pref_map[pref_sum-k]
            res_max = max(res_max,length)
        if pref_sum not in pref_map:
            pref_map[pref_sum]=i
    return res_max
arr = list(map(int,input().split()))
k=int(input())
print(long_subarr(arr,k))
