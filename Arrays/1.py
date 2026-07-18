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