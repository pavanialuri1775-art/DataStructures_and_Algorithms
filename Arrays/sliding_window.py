s=['a','i','o', 'r','t','u' ,'o']
k=4
vowels="aeiouAEIOU"
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