def hasTripletSum(arr, target):
    arr.sort()
    for i in range(len(arr)-2):
        left=i+1
        right=len(arr)-1
        while left<right:
            pref_sum=arr[i]+arr[left]+arr[right]
            if pref_sum==target:
                return True
            elif pref_sum<target:
                left+=1
            else:
                right-=1
    return False
                