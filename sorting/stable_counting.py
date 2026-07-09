#1 class Solution:
def stable_count_sort(arr):#[2,3,2,4,3]
    max_ele=max(arr)
    count=[0]*(max_ele+1)#[0,0,0,0,0]
    for num in arr:
        count[num]+=1  #[0,0,2,2,1,2]
    for i in range(1,len(count)):
        count[i]+=count[i-1] #[0,0,2,4,5,7]
    output=[0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        ele=arr[i]
        position=count[ele]-1
        output[position]=ele
        count[ele]-=1  
    return output   
arr=list(map(int,input().split()))
print(stable_count_sort(arr))