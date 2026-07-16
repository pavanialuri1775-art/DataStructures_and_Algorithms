#prefix_sum:A prefix sum stores the sum of all elements from the beginning up to the current index.

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
