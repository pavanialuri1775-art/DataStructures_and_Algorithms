s=['a','i','o', 'r','t','u' ,'o']
k=4
vowels="aeiou"
win_count=0
max_count=0
for i in range(k):
    if s[i] in vowels:
        win_count+=1
max_count=win_count
for i in range(k,len(s)):
    if s[i-k] in vowels:
        win_count-=1
    if s[i] in vowels:
        win_count+=1
    max_count=max(max_count,win_count)
print(max_count)

#2  maxsum subarray with length k
arr=[3,-2,5,-1,6,-3,2,7,-5]
k=6
win_sum=sum(arr[:k])
max_sum=win_sum
for i in range(k,len(arr)):
    win_sum+=arr[i]-arr[i-k]
    max_sum=max(win_sum,max_sum)
print(max_sum)

#
def is_prime(n):#10
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):#2,3
        if n%i==0:#30%2==0
            return False
    return True
for i in range(2,31):
    if is_prime(i):
        print(i,end=" ")#2
        
#highest subarray sum of length 3
# time complexity--------o(n)^3
arr=list(map(int,input().split()))
n=len(arr)
ans=0
sub_arr_len=3
for i in range(n):
    for j in range(i,n):
        temp=[]
        tsum=0
        for k in range(i,j+1):
            temp.append(arr[k])
            tsum+=arr[k]
        if len(temp)==sub_arr_len:
            ans=max(ans,tsum)
print(ans)

#
def sliding_win(arr,k):
    n=len(arr)
    left=0
    win_sum=sum(arr[:k])
    max_sum=win_sum
    for right in range(k,n):
        win_sum+=arr[right]
        win_sum-=arr[left]
        left+=1
        max_sum=max(max_sum,win_sum)
    return max_sum
arr=list(map(int,input().split()))
k=int(input())
print(sliding_win(arr,k))

#Substrings of Size Three with Distinct Characters
#brute force----
#time complexity------0(n)^3
s="aababcabc"
n=len(s)
k=3
count=0
for i in range(n):
    for j in range(i,n):
        temp=""
        for k in range(i,j+1):
            temp+=s[k]
        if len(temp)==3 and len(set(temp))==len(temp):
            count+=1
print(count)

#time complexity--0(n)
s="aababcabc"
n=len(s)
left=0
ans=0
k=3
dic={}
for r in range(n):
    if s[r] in dic:
        dic[s[r]]+=1
    else:
        dic[s[r]]=1
    
    if r-left==k:
        dic[s[left]]-=1
        if dic[s[left]]==0:
            dic.pop(s[left])
        left+=1
        
    if len(dic)==k:
        ans+=1
        
print(ans)
        
