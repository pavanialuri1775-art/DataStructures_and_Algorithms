#Anagram Check
#Two strings are anagrams if they contain the same characters with the same frequencies.
'''def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    count={}
    for ch in s1:
        count[ch]=count.get(ch,0)+1
    for ch in s2:
        if ch not in count:
            return False
        count[ch]-=1
    for value in count.values():
        if value!=0:
            return False
    return True
s=input()
r=input()
print(anagram(r,s))

#First Non-Repeating Character
def first_non_repeating(s):  
    count={}
    for ch in s:
        count[ch]=count.get(ch,0)+1
    for ch in s:
        if count[ch]==1:
            return ch
            break
    return -1
s=input()
print(first_non_repeating(s))'''

#Two Sum
def two_sum(nums,target):
    n=len(nums)
    for i in range(n-1):
        for j in range(1,n-1):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []
nums=list(map(int,input().split()))
target=int(input())
print(two_sum(nums,target))
                
    

