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

#
def sort012(self, arr):
    low=0
    mid=0
    high=len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr
                