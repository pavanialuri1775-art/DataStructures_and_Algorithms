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
    