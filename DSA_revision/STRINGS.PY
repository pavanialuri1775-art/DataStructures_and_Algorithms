#Count Vowels
def count_vowels(s):
    vowels="AEIOUaeiou"
    count=0
    for ch in s:
        if ch in vowels:
            count+=1
    return count
s=input()
print(count_vowels(s))

#Reverse a String
def reverse_str(s):
    arr=list(s)
    left=0
    right=len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right+=1
    return " ".join(arr)
s=input()
print(reverse_str(s))

#
def reverse_str(s):
    res=""
    for i in range(len(s)-1,-1,-1):
        res+=s[i]
    return  res
s=input()
print(reverse_str(s)) ''' 

#Key of Minimum Value
'''Problem Statement: Write a Python program to find the key associated with the smallest numerical value in a dictionary.
Given Input:
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
min_value=min(stock.values())
for key,value in stock.items():
    if value==min_value:
        print("last stock key:",key)
        
#
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
min_value=min(stock.values())
for key in stock.keys():
    if stock[key]==min_value:
        print("last stock key:",key)
        
#
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
min_key=None
min_value=float('inf')
for key,value in stock.items():
    if value<min_value:
        min_value=value
        min_key=key
print(min_key)

#Palindrome Check
def is_palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
s=input()
print(is_palindrome(s))